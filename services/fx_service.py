import asyncio
import time
from enum import Enum
from threading import Lock

import aiohttp
import requests
from fastapi import FastAPI
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

app = FastAPI()
app.fx_rates = {}
app.latest_update_timestamp = None
app.currencies = {"USD", "EUR", "GBP", "BPI"}
app.coindesk_session = None

coindesk_service_uri = 'https://api.coindesk.com/v1/bpi/currentprice.json'

#fx_rates_lock = Lock()
fx_rates_lock = asyncio.Lock()

class ErrorCodes(Enum):
    FX_RATES_SERVICE_ERROR = 1
    FX_RATES_UPDATED = 2
    INVALID_INPUT_PARAMETERS = 3

# Note: this function is defined as async to demonstrate the overall approach for interatcing with IO intensive external services
# However, in reality, this could result in the CoindDesk service getting called several times in a quick succession and hence in less performance optimization
async def update_rates():

    logging.info("Invoking the external Coind Desk REST API")

    #the async http client session is cached to reuse its Thread Pool
    if app.coindesk_session is None:
        app.coindesk_session = aiohttp.ClientSession()
    response = await app.coindesk_session.get(coindesk_service_uri)

    #alternative way to invoke the http client without caching
    #async with aiohttp.ClientSession() as session:
    #    async with session.get(coindesk_service_uri) as response:
    #        json_body = await response.json()
    #    print(json_body)

    if response.status != 200:
        return ErrorCodes.FX_RATES_SERVICE_ERROR
    else:
        json_body = await response.json()

        for d in json_body["bpi"]:

            cur = json_body["bpi"][d]

            logging.info(cur)
            logging.info(cur)
            logging.info(cur["code"])
            logging.info(cur["rate_float"])

            if cur["code"] == "USD":
                bpi_usd = float(cur["rate_float"])

            if cur["code"] == "EUR":
                bpi_eur = float(cur["rate_float"])

            if cur["code"] == "GBP":
                bpi_gbp = float(cur["rate_float"])

    # acquire the lock
    async with fx_rates_lock:

        app.fx_rates["BPI_USD"] = bpi_usd
        app.fx_rates["USD_BPI"] = 1/bpi_usd

        app.fx_rates["BPI_EUR"] = bpi_eur
        app.fx_rates["EUR_BPI"] = 1/bpi_eur

        app.fx_rates["BPI_GBP"] = bpi_gbp
        app.fx_rates["GBP_BPI"] = 1/bpi_gbp


        app.fx_rates["EUR_USD"] = bpi_usd/bpi_eur
        app.fx_rates["USD_EUR"] = bpi_eur/bpi_usd

        app.fx_rates["GBP_USD"] = bpi_usd/bpi_gbp
        app.fx_rates["USD_GBP"] = bpi_gbp/bpi_usd

        app.fx_rates["EUR_GBP"] = bpi_gbp/bpi_eur
        app.fx_rates["GBP_EUR"] = bpi_eur/bpi_gbp

    app.latest_update_timestamp = time.time()

    logging.info(app.fx_rates)

    return ErrorCodes.FX_RATES_UPDATED

def check_cache_staleness():

    if app.latest_update_timestamp is None:
        return True

    ct = time.time()
    elapsed_time = ct - app.latest_update_timestamp
    logging.info(f'Elapsed time since last cache update: {elapsed_time} seconds')

    if elapsed_time >= 3600:
        return True
    else:
        return False

@app.get("/")
async def read_root():

    async with fx_rates_lock:
        return app.fx_rates.copy()

@app.get("/v1/all-current-fx-rates")
async def get_all_current_fx_rates():

    async with fx_rates_lock:
        return app.fx_rates.copy()

@app.get("/v1/all-latest-fx-rates")
async def get_all_latest_fx_rates():

    await update_rates()

    async with fx_rates_lock:
        return app.fx_rates.copy()


#http://127.0.0.1:8000/v1/converted-amount/?ccy_from=USD&ccy_to=GBP&quantity=1000
@app.get("/v1/converted-amount/")
async def fx_convert(ccy_from: str , ccy_to: str, quantity: float):

    #validate the input parameters
    if ccy_from in app.currencies and ccy_to in app.currencies and quantity > 0:

        cache_state_stale = check_cache_staleness()

        if cache_state_stale:
           cache_update_state = await update_rates()
        else:
            cache_update_state = ErrorCodes.FX_RATES_UPDATED

        if cache_update_state != ErrorCodes.FX_RATES_UPDATED:
            return {"error": cache_update_state}

        cur_pair = ccy_from + "_" + ccy_to

        async with fx_rates_lock:
            fx_rate = app.fx_rates[cur_pair]

        converted_quantity = round(quantity * fx_rate, 2)

        return {"quantity": converted_quantity, "ccy": ccy_to}

    else:
        #if incorrect input parameters submitted to the service, then return json with blank attribute values
        logging.info("incorrect input parameter values")
        return {"error": ErrorCodes.INVALID_INPUT_PARAMETERS}
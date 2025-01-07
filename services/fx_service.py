import time
from enum import Enum
from threading import Lock
import requests
from fastapi import FastAPI
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

app = FastAPI()
app.fx_rates = {}
app.latest_update_timestamp = None
app.currencies = {"USD", "EUR", "GBP", "BPI"}

coindesk_service_uri = 'https://api.coindesk.com/v1/bpi/currentprice.json'

fx_rates_lock = Lock()

class ErrorCodes(Enum):
    FX_RATES_SERVICE_ERROR = 1
    FX_RATES_UPDATED = 2
    INVALID_INPUT_PARAMETERS = 3

def update_rates():

    raw_resp = requests.get(url=coindesk_service_uri)

    if raw_resp.status_code != 200:
        return ErrorCodes.FX_RATES_SERVICE_ERROR
    else:
        r = raw_resp.json()

        for d in r["bpi"]:

            cur = r["bpi"][d]

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
    with fx_rates_lock:

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

    logging.info(app.fx_rates)

    return ErrorCodes.FX_RATES_UPDATED

def check_cache_staleness():

    if app.latest_update_timestamp is None:
        update_status =  update_rates()
        if update_status == ErrorCodes.FX_RATES_SERVICE_ERROR:
            return update_status
        else:
            app.latest_update_timestamp = time.time()
            return ErrorCodes.FX_RATES_UPDATED
    else:
        ct = time.time()
        elapsed_time = ct - app.latest_update_timestamp
        logging.info('Elapsed time:', elapsed_time, 'seconds')

        if elapsed_time >= 3600:
            update_status = update_rates()
            if update_status == ErrorCodes.FX_RATES_SERVICE_ERROR:
                return update_status
            app.latest_update_timestamp = time.time()

        return ErrorCodes.FX_RATES_UPDATED


@app.get("/")
async def read_root():

    with fx_rates_lock:
        return app.fx_rates.copy()

@app.get("/v1/all-current-fx-rates")
async def get_all_current_fx_rates():

    with fx_rates_lock:
        return app.fx_rates.copy()

@app.get("/v1/all-latest-fx-rates")
async def get_all_latest_fx_rates():

    update_rates()

    with fx_rates_lock:
        return app.fx_rates.copy()


#http://127.0.0.1:8000/v1/converted-amount/?ccy_from=USD&ccy_to=GBP&quantity=1000
@app.get("/v1/converted-amount/")
async def fx_convert(ccy_from: str , ccy_to: str, quantity: float):

    #validate the input parameters
    if ccy_from in app.currencies and ccy_to in app.currencies and quantity > 0:

        cache_state = check_cache_staleness()

        if cache_state != ErrorCodes.FX_RATES_UPDATED:
            return {"error": cache_state}

        cur_pair = ccy_from + "_" + ccy_to

        with fx_rates_lock:
            fx_rate = app.fx_rates[cur_pair]

        converted_quantity = round(quantity * fx_rate, 2)

        return {"quantity": converted_quantity, "ccy": ccy_to}

    else:
        #if incorrect input parameters submitted to the service, then return json with blank attribute values
        logging.info("incorrect input parameter values")
        return {"error": ErrorCodes.INVALID_INPUT_PARAMETERS}
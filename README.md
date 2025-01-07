# **Currency Converter REST API service**

Users can send GET requests to the Currency Converter REST API with parameters
ccy_from=USD&amp;ccy_to=GBP&amp;quantity=1000 and receive a response in the JSON format {“quantity”: 779.77,
“ccy”: “GBP”}.

The service is using near-real-time FX rates that are derived from the CoinDesk REST API
(https://api.coindesk.com/v1/bpi/currentprice.json). This service provides real-time bitcoin prices in 3
currencies (USD, EUR, GBP). FX rates are derived e.g. as EUR/USD = BPI_USD/BPI_EUR. 

**Error conditions, error messages and codes returned by the service:**

    FX_RATES_SERVICE_ERROR = 1
    INVALID_INPUT_PARAMETERS = 3

Error Condition - Invalid Input Parameters:
{"error": ErrorCodes.INVALID_INPUT_PARAMETERS}

Error Condition - The FX Rates in the LOcal Cache are stale and when tried was unable to obtain the latest FX Rates from the CoinDesk Service:
{"error": ErrorCodes.FX_RATES_SERVICE_ERROR }

The Currency Converter Service implementation is based on the FastAPI framework

Data Caching Capabilities of the service - Because it is safe to assume that FX rates are changing once an hour, there is opportunity to supply the service with 
data caching capability and thus improve its performance. The service caches the fx rates for 60 min and the cached data is reused across all service requests during 
that time period, thus avoiding to call each time the remote CoinDesk service for each request to the Currency Converter Service  

There are two architecture options for data caching for this service:

**a) Local Data Caching**

This is currently implemented within each FastAPI Worker instance of the service (and hence the name "local" cache ie a cache bound/individual to each worker instance)

The local cache is refreshed automatically, when the next invocation of the service encounters that the cache is stale if at least 60 min have elapsed since the 
previous cache reload/refresh 

The local cache is based on the python dictionary (hashmap) internal/native data structure, which is threadsafe for the basic / atomic operations such as read item or add/update item
In addition to that the service is implemented with the async def endpoint flavour of the FastAPI Framework - this limits the execution of the service strictly on a single thread in a Node.js style
and hence avoids multithreading issues when accessing shared data structures 

For the non-async def FastAPI endpoint -  Non-async def endpoints (i.e., plain def endpoints) get executed in a threadpool, so it is possible to run into 
thread safety issues if the code makes modifications to shared global objects or similar. However, reiterate again, in the current python Cpyton implementation, the basic/atomic
operations of dictionary are threadsafe 

Finally, despite all of the above analysis which demonstrates that a dictionary based, local data cache implementation is threadsafe for both end point flavours of FastAPI, 
the service implements a Lock based access to the data cache for futureproof evolution of the product and to demonstrate methods for threadsafe access to shared data structures

**b) Global Data Caching**

for Global Cache shared between all FastAPI Worker Instances (each Worker is a separate OS Process, which can run on the same or different server machine)
the solution can use Reddis and specifically Reddis with local cache deployment and use 
https://redis.io/docs/latest/develop/clients/client-side-caching/

This is outlined for info only and is currently not implemented in the service
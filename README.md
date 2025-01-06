# **Currency Converter REST API service**

Users can send GET requests to the Currency Converter REST API with parameters
ccy_from=USD&amp;ccy_to=GBP&amp;quantity=1000 and receive a response in the JSON format {“quantity”: 779.77,
“ccy”: “GBP”}.

The service is using near-real-time FX rates that are derived from the CoinDesk REST API
(https://api.coindesk.com/v1/bpi/currentprice.json). This service provides real-time bitcoin prices in 3
currencies (USD, EUR, GBP). FX rates are derived e.g. as EUR/USD = BPI_USD/BPI_EUR. It is safe to
assume that FX rates are changing once an hour.


for Global Cache shared between all FAstAPI Workers (each Worker is a separate OS Process, which can run on the same or different server machine)
the solution can use Reddis and specifically Reddis with local cache deployment and use 
https://redis.io/docs/latest/develop/clients/client-side-caching/
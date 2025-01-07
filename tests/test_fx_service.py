import requests
import pytest

# The service needs to be tested with its caching functionality but the cach doesnt persist when using the FastAPI TestClient, since it invokes
#the service API methods directly as in process python function call and hence there is no constantly running service process to mainatin the cach.
#Hence the test suite doesnt use the FastAPI TestClient

class TestSequence:

    currency_pairs = ["BPI_USD", "USD_BPI", "BPI_EUR", "EUR_BPI", "BPI_GBP", "GBP_BPI",
                      "EUR_USD", "USD_EUR", "GBP_USD", "USD_GBP", "EUR_GBP", "GBP_EUR"]

    test_currency_quantity = 100000

    fx_rates = None
    @pytest.mark.dependency(name="test_get_the_latest_fx_rates")
    def test_get_the_latest_fx_rates(self):

        fx_rates_service_uri = 'http://127.0.0.1:8000/v1/all-latest-fx-rates'

        resp = requests.get(url=fx_rates_service_uri)
        assert resp.status_code == 200

        TestSequence.fx_rates = resp.json()

        print(TestSequence.fx_rates)

        for cur_pair in TestSequence.currency_pairs:
            print(TestSequence.fx_rates[cur_pair])

    @pytest.mark.dependency(name="test_get_the_latest_fx_rates")
    def test_cur_conversion(self):

        for cur_pair in TestSequence.currency_pairs:

            ct = cur_pair.split("_")

            from_cur = ct[0]
            to_cur = ct[1]

            fx_conversion_service_uri = f"http://127.0.0.1:8000/v1/converted-amount/?ccy_from={from_cur}&ccy_to={to_cur}&quantity={TestSequence.test_currency_quantity}"

            resp = requests.get(url=fx_conversion_service_uri)
            assert resp.status_code == 200

            converted_quantity_response = resp.json()

            print(converted_quantity_response["quantity"])
            print(converted_quantity_response["ccy"])

            assert to_cur == converted_quantity_response["ccy"]

            fx_rate = TestSequence.fx_rates[cur_pair]

            assert round(float(fx_rate) * TestSequence.test_currency_quantity, 2) == float(converted_quantity_response["quantity"])

    @pytest.mark.dependency(name="test_cur_conversion")
    def test_invalid_input_params(self):

        #deliberatly misformatted service input params
        from_cur = "GB"
        to_cur = ""
        invalid_quantity = 0

        fx_conversion_service_uri = f"http://127.0.0.1:8000/v1/converted-amount/?ccy_from={from_cur}&ccy_to={to_cur}&quantity={invalid_quantity}"

        resp = requests.get(url=fx_conversion_service_uri)
        assert resp.status_code == 200

        converted_quantity_response = resp.json()

        assert converted_quantity_response["error"] == 3

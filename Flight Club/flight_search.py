import os
import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    """Class created for flight search operations. Includes functions for amadeus api authentication,
    fetching iata codes for destination cities from amadeus API"""
    def __init__(self):
        self.headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        self.endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    def get_auth_token(self):
        """Retrieves authentication Bearer Access Token"""
        endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        parameters = {
            "grant_type": "client_credentials",
            "client_id": f"{os.getenv('amadeus_client_id')}",
            "client_secret": f"{os.getenv('amadeus_client_secret')}",
        }
        print("[#] Amadues API Authentication in Progress")
        response = requests.post(url=endpoint, headers=self.headers, data=parameters)
        auth_token = response.json()
        return auth_token['access_token']

    def get_iata_code(self, city_name, access_token):
        """Fetches iata codes for flight destination cities for given ids"""
        endpoint = self.endpoint
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer    {access_token}"
        }
        parameters = {
            "keyword": city_name
        }
        response = requests.get(url=endpoint, params=parameters, headers=headers)
        try:
            IATA = response.json()
        except IndexError:
            print(f"[-] IndexError: No Airport Code Found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"[-] KeyError: No Airport Code Found for {city_name}")
            return "Not Found"
        else:
            return IATA["data"][0]["iataCode"]

import os
import requests
import json
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    """Class created for spreadsheet operations. Includes functions for fetching, checking, printing and filling data
    from the sheety API"""
    def __init__(self):
        self.endpoint = "https://api.sheety.co/aa827fab97abc7faffe53e4441caf81b/flyCheap/prices"
        self.headers = {
            "Authorization": f"{os.getenv('sheety_auth')}",
            "Content-Type": "application/json"
        }

    def get_data(self):
        """Fetches data from the Google spreadsheet linked with sheety API"""
        response = requests.get(url=self.endpoint, headers=self.headers)
        data = response.json()
        print("[#] Fetching User Database")
        return data

    def put_data(self, id_info, iata_info):
        """Populates the iata codes for cities in the Google spreadsheet"""
        endpoint = f"https://api.sheety.co/aa827fab97abc7faffe53e4441caf81b/flyCheap/prices/{id_info}"
        body = {
            "price": {
                "iataCode": iata_info
            }
        }
        requests.put(url=endpoint, headers=self.headers, data=json.dumps(body))

    def print_sheet(self):
        """Prints the current instance of Google spreadsheet"""
        print_sheet = self.get_data()
        print_sheet = print_sheet["prices"]
        return print_sheet

    def get_customer_emails(self):
        """ Fetches customer email addresses from the Google spreadsheet and Google forms"""
        endpoint = "https://api.sheety.co/aa827fab97abc7faffe53e4441caf81b/flyCheap/users"
        response = requests.get(url=endpoint, headers=self.headers)
        data = response.json()
        print("[#] Fetching Customer Emails")
        return data

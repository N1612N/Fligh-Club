import requests
import datetime


class TicketPrices:
    """This class deals with the searching of flight tickets with given requirements by the user"""
    def __init__(self, access_token):
        self.access_token = access_token

        self.endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.today = datetime.date.today()
        self.originLocationCode = "LON"
        self.departureDate = self.today + datetime.timedelta(days=+1)
        self.returnDate = self.today + datetime.timedelta(weeks=+32)
        self.adults = 1
        self.currencyCode = "GBP"
        self.nonStop = "true"
        self.max = 1

    def get_offers(self, destination_location, max_price):
        """Gets available fights with offers for given requirements from amadeus"""
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer    {self.access_token}"
        }
        parameters = {
            "originLocationCode": self.originLocationCode,
            "destinationLocationCode": destination_location,
            "departureDate": self.departureDate,
            "returnDate": self.returnDate,
            "adults": self.adults,
            "nonStop": self.nonStop,
            "currencyCode": self.currencyCode,
            "maxPrice": max_price,
            "max": self.max
        }
        response = requests.get(url=self.endpoint, params=parameters, headers=headers)
        offers = response.json()
        return offers

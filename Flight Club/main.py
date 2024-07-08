from art import banner_image
from art import banner_text
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import TicketPrices
from notification_manager import NotificationManager

# Print welcome art in console
print(banner_image)
print(banner_text)

# Construct sheety object for spreadsheet operations
sheety = DataManager()
sheety_data = sheety.get_data()
sheet_data = sheety_data["prices"]
print("[+] Data Fetched Successfully")

# Construct flight object for flight operations
flight = FlightSearch()
access_token = flight.get_auth_token()
print(f"[*] Access Token Retrieved: {access_token}")
print("[+] Authentication Successful")

print("[#] Validating IATA Codes")
for city in sheet_data:
    # Validate if the IATA code is available in the sheet, if not populate the sheet
    if city['iataCode'] == "":
        print(f"[#] Fetching IATA Code for {city['city']}")
        city['iataCode'] = flight.get_iata_code(city["city"], access_token)
        item_id = city['id']
        info = city['iataCode']
        sheety.put_data(item_id, info)
print(f"[+] IATA Codes Validation Successful")

# print updated sheet data
updated_sheet = sheety.print_sheet()

# Construct ticket object to check for the flight ticket offers
ticket_offers = TicketPrices(access_token)

# Construct a notification object to send sms notifications
notification = NotificationManager()

# Get customer information from sheety users spreadsheet
customer_data = sheety.get_customer_emails()
customer_data = customer_data['users']

customer_emails_list = []

# Adding customer email addresses to a list
for customer in customer_data:
    email_address = customer['whatIsYourEmailAddress?']
    customer_emails_list.append(email_address)

# for every ticket offer send a sms to personal mobile number
for city in updated_sheet:
    destination = city["iataCode"]
    max_price = city["lowestPrice"]
    try:
        # Get Flight ticket offers from amadeus flight search
        offer = ticket_offers.get_offers(destination, max_price)
        # Sort the offer information
        offer_price = offer["data"][0]['price']["total"]
        offer_currency = offer["data"][0]['price']["currency"]
        on_date = offer["data"][0]['lastTicketingDate']
        source_port = offer["data"][0]['source']
    except IndexError:
        # Catch error for cities with no flight available
        print(f"[!] No Tickets Available for {city['city']}")
    else:
        print(f"[+] Tickets Available for {city['city']}")
        message_body = (f"Fly with us on {on_date} from {source_port} to {destination} "
                        f"for just {offer_price} {offer_currency}. Enjoy a Roundtrip Offer valid for next 180 Days.\n"
                        f"~ Coconut Holidays")
        # Send Mail notifications to all the users with flight offer details
        for email in customer_emails_list:
            customer_email_address = email
            notification.send_mail(customer_email_address, message_body)

        # Send SMS notification to the user with flight offer details
        notification.send_mesg(message_body)

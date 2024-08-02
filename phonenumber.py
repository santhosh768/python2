import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Prompt the user to enter a phone number with the country code
mobile_no = input("Enter phone number with country code (+xx xxxxxxxxx): ")

# Parse the phone number
try:
    phone_number = phonenumbers.parse(mobile_no)

    # Check if the number is valid
    if phonenumbers.is_valid_number(phone_number):
        # Get the timezone
        time_zones = timezone.time_zones_for_number(phone_number)
        print('Time Zones:', ', '.join(time_zones))

        # Get the carrier information
        service_provider = carrier.name_for_number(phone_number, "en")
        print('Service Provider:', service_provider)

        # Get the location
        country = geocoder.description_for_number(phone_number,"en")
        print('Country:', country)
    else:
        print("Invalid phone number. Please try again.")
except phonenumbers.NumberParseException:
    print("Invalid phone number format. Please enter the number in the correct format.")

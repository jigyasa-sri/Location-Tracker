import phonenumbers as ph
from phonenumbers import geocoder as geo
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import geocoder as gc
import folium
import os

PHONE_NUMBER = "phone_number"
IP = "IP_address"
KEY = "0123456sfdgfhgj"  # ENTER YOUR API_KEY HERE
choice = input("Locate by phone_number, IP_address: ")
location = []
location_details = "India"

if os.path.exists("mylocation.html"):
    os.remove("mylocation.html")

if choice.lower() == PHONE_NUMBER:
    try:
        phone_number = input("Enter valid Phone number: ")
        number = ph.parse(phone_number)
        location_details = geo.description_for_number(number, "en")
        carrier_name = carrier.name_for_number(number, "en")
        print(number)
        print(location_details)
        print(carrier_name)
        geoCode = OpenCageGeocode(KEY)
        query = str(location_details)
        result = geoCode.geocode(query)
        lat = result[0]['geometry']['lat']
        lang = result[0]['geometry']['lng']
        location = [lat, lang]
    except:
        print("Something went wrong..")
        print("Please Enter valid Number with country Code")

elif choice == IP:
    geoLocation = gc.ip('me')
    location = geoLocation.latlng

else:
    print("I am sorry something went wrong try again")

if len(location):
    my_map = folium.Map(location=location, zoom_start=12)
    folium.Marker(location, popup=location_details).add_to(my_map)
    my_map.save('mylocation.html')

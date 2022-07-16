import requests
from datetime import datetime

import timezones

time_zones = timezones.time_zones

def get_zones():
     for zones in time_zones.items():
        print(zones)

zones = get_zones()


def get_input():
    
    # Displays all time zones
    
    print(zones)
    
    print("Select timezone by entering number.")
    val = int(input("Here: "))

    # Apportion user input as the time zone
    
    zone = time_zones[val]
    url = 'http://worldtimeapi.org/api/timezone/' + zone
    # print(url)

    # To request the url in JSON format
    
    request = requests.get(url)
    jsonFormat = request.json()
    # print(jsonFormat)

    # Rendering the JSON format in the console

    # time = datetime.strptime(date_time, "%m-%d-%Y")
    # print(type(time))


    print("Time zone: ", jsonFormat['timezone'])
    print("Date Time: ", jsonFormat['datetime'])
    print("Abbr: ", jsonFormat['abbreviation'])
    print("UTC Date Time: ", jsonFormat['utc_datetime'])
    print("Week Number: ", jsonFormat['week_number'])

    
get_input()





















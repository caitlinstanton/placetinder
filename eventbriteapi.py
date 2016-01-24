import requests
import json,csv

EVENTBRITE_OAUTH_TOKEN = 'FN34EGTLTCYGHBDNRIKB'
url = "https://www.eventbriteapi.com/v3/"

def search(query, coordinates, radius, price, startDate, endDate):
    """
    Search the Eventbrite API for the top events that match the given parameters.
    Args:
        query (str): The query to search for events. If left an empty string, all events are searched.
        coordinates (str): The latitude and longitude, separated by a comma.
        radius (str): The radius around the coordinates to search within, in miles.
        price (str): The price of the event, either "free" or "paid".
        startDate (str): The earliest possible UTC time and date, in the form yyyy-mm-dd;hh:mm (24-hour clock).
        endDate (str): The latest possible UTC time and date, in the form yyyy-mm-dd;hh:mm (24-hour clock).
    Returns:
        queried: A list of the JSON responses from events that match the search query.
	Creates:
		eventbrite.csv: A CSV file of the information for all of the objects in queriedevents.
    """
    res = requests.get(
        url + "events/search/",
            headers = {"Authorization": "Bearer " + EVENTBRITE_OAUTH_TOKEN},
	    params = {
            "q": query,
            "sort_by": "best",
            "location.latitude": coordinates[:coordinates.index(",")],
            "location.longitude": coordinates[coordinates.index(",")+1:],
            "location.within": radius + "mi",
            "price": price,
            "start_date.range_start": startDate + "T00:00:00",
            "start_date.range_end": endDate + "T00:00:00"
        }
    )

    queriedevents = res.json()["events"]
    return queriedevents

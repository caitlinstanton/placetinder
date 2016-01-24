import requests
import json,csv

EVENTBRITE_OAUTH_TOKEN = 'FN34EGTLTCYGHBDNRIKB'
url = "https://www.eventbriteapi.com/v3/"

def search(query, location, price, startDate,startTime):
    """
    Search the Eventbrite API for the top events that match the given parameters.
    Args:
        query (str): The query to search for events. If left an empty string, all events are searched
        location (str): The location of the user (found through geolocation). Searches for events taking place in the same region
        price (str): The price of the event, either "free" or "paid"
        startDate (str): The requested UTC start date of the event, in the form yyyy-mm-dd
        startTime (str): The requested UTC start date of the event, in the form hh:mm:ss (24-hour clock).
    Returns:
        queried: A list of the JSON responses from events that match the search query
	Creates:
		eventbrite.csv: A CSV file of the information for all of the objects in queriedevents
    """
    res = requests.get(
        url + "events/search/",
            headers = {"Authorization": "Bearer " + EVENTBRITE_OAUTH_TOKEN},
	    params = {
            "q": query,
            "sort_by":"best",
	        "venue.region": location,
			"price": price,
			"start_date.range_start":startDate + "T" + startTime
	    }
    )

    queriedevents = res.json()["events"]

    with open('eventbrite.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        for event in queriedevents:
            name = event['name']['text'].encode('utf-8').strip()
            description = event["description"]["text"].encode('utf-8').strip() 
            eventurl = event["url"]
            startdate = event["start"]["local"]
            enddate = event["end"]["local"]
            spamwriter.writerow((name, description, eventurl, startdate, enddate))
	
	return queriedevents

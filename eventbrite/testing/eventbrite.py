import requests
import json,csv

EVENTBRITE_OAUTH_TOKEN = 'FN34EGTLTCYGHBDNRIKB'
url = "https://www.eventbriteapi.com/v3/"

def search(query, coordinates, price, startDate,startTime):
    res = requests.get(
        url + "events/search/",
	    headers = {"Authorization": "Bearer " + EVENTBRITE_OAUTH_TOKEN},
	    params = {
            "q": query,
            "sort_by":"best",
	        "venue.city": coordinates,
			"price":price,
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
			
search("concert","london","paid","2016-01-23","07:30:00")
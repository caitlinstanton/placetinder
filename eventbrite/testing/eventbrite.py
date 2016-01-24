import requests
import os
import csv

"""
search(hashtag)

Input:
hashtag - String that will be searched for.

Output:
Returns nothing, but writes search results in tweets.csv.
"""

def search(type):
  
    EVENTBRITE_OAUTH_TOKEN = 'JYHSYPNUFM546GH2YJSO'

    url = "https://www.eventbriteapi.com/v3/events/search.?popular=yes&token=JYHSYPNUFM546GH2YJSO"

    res = requests.post(
	    url,
	    params = {
	        "event.online_event" : True,
	    }
    )

    print res['events']
	
    """
    events = res.json()['events'][0]
    with open('events.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in events:
            content = i.name.text.encode('utf-8').strip() + "<br><br>"
            spamwriter.writerow((content))
            print i.name.text

    """
hashtag = raw_input("what hash do you want to search?\n")

search(hashtag)
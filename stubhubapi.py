import urllib2, json

API_URL = "https://api.stubhub.com/search/catalog/events/v3"
APPLICATION_TOKEN = "VsLaqXIQj3mygZTo36tu5rcoxkEa"

def searchQuery(query):
    """
    Search the StubHub API for all events that match a search query.
    Args:
        query (str): The search query.
    Returns:
        list: A list of the JSON responses from all events that match the search query.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url = API_URL + "?q=" + query.replace(" ", "+")
    headers = {"Authorization":"Bearer " + APPLICATION_TOKEN,
               "Accept":"application/json",
               "Accept-Encoding":"application/json"}
    request = urllib2.Request(url, None, headers)
    result = urllib2.urlopen(request).read()
    r = json.loads(result)
    return r["events"]

def search(eventType, coordinates, radius, price, earliestTime, latestTime):
    """
    Search the StubHub API for all events that match the given parameters.
    Args:
        eventType (str): The type of event (Concerts, Sports, Theater, etc.).
        coordinates (str): The latitude and longitude, separated by a comma.
        radius (float): The radius around the coordinates to search within.
        price (float): The approximate price in dollars.
        earliestTime (str): The earliest possible time and date.
        latestTime (str): The latest possible time and date.
    """
    

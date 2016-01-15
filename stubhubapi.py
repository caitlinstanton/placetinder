import urllib2, json

API_URL = "https://api.stubhub.com/search/catalog/events/v3"
APPLICATION_TOKEN = "VsLaqXIQj3mygZTo36tu5rcoxkEa"

def searchQuery(query, num):
    """
    Search the StubHub API for a number of events that match a search query.
    Args:
        query (str): The search query.
        num (int): The number of events to return (maximum 500).
    Returns:
        list: A list of the JSON responses from events that match the search query.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url = API_URL + "?rows=" + str(num)
    url += "&q=" + query.replace(" ", "+")
    headers = {"Authorization":"Bearer " + APPLICATION_TOKEN,
               "Accept":"application/json",
               "Accept-Encoding":"application/json"}
    request = urllib2.Request(url, None, headers)
    result = urllib2.urlopen(request).read()
    r = json.loads(result)
    return r["events"]

def search(eventType, coordinates, radius, price, earliestTime, latestTime):
    """
    Search the StubHub API for the top 500 events that match the given parameters.
    Args:
        eventType (str): The type of event (Concert, Sports, Theater, etc.).
        coordinates (str): The latitude and longitude, separated by a comma.
        radius (float): The radius around the coordinates to search within, in miles.
        price (float): The approximate price in dollars.
        earliestTime (str): The earliest possible time and date, in the form yyyy-mm-dd;hh:mm:ss (24-hour clock).
        latestTime (str): The latest possible time and date, in the form yyyy-mm-dd;hh:mm:ss (24-hour clock).
    Returns:
        list: A list of the JSON responses from events that match the search query.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url = API_URL + "?rows=500"
    url += "&q=" + eventType # Must manually verify that event type matches
    url += "&point=" + coordinates
    url += "&radius=" + str(radius) # Must manually verify that event is in radius
    # Manually check for price
    url += "&sort=eventDateLocal+asc"
    # Manually check for date, use "start" parameter to go to next results if they exist
    headers = {"Authorization":"Bearer " + APPLICATION_TOKEN,
               "Accept":"application/json",
               "Accept-Encoding":"application/json"}
    request = urllib2.Request(url, None, headers)
    result = urllib2.urlopen(request).read()
    r = json.loads(result)
    print len(r["events"])
    print r["events"][0]
    return r["events"]

search("", "44.680239,-68.803044", 0, 0, 0, 0)

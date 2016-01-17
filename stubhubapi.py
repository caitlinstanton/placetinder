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

def search(eventType, coordinates, radius, minPrice, maxPrice, earliestTime, latestTime):
    """
    Search the StubHub API for the top 500 events that match the given parameters.
    Args:
        eventType (str): The broad category of event (Concert, Sports, Theater, or Arts). If none is specified, all events are searched.
        coordinates (str): The latitude and longitude, separated by a comma.
        radius (float): The radius around the coordinates to search within, in miles.
        minPrice (float): The minimum price in dollars.
        maxPrice (float): The maximum price in dollars.
        earliestTime (str): The earliest possible time and date, in the form yyyy-mm-dd;hh:mm:ss (24-hour clock).
        latestTime (str): The latest possible time and date, in the form yyyy-mm-dd;hh:mm:ss (24-hour clock).
    Returns:
        list: A list of the JSON responses from events that match the search query.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url = API_URL + "?rows=500&status=active"
    if eventType != "":
        url += "&q=" + eventType
        if eventType == "Theater" or eventType == "Arts":
            eventType = "Theater tickets and Arts"
    url += "&point=" + coordinates
    url += "&radius=" + str(radius)
    url += "&fieldList=*,ticketInfo"
    url += "&sort=eventDateLocal+asc"
    # To do: manually check for date, use "start" parameter to go to next results if they exist
    headers = {"Authorization":"Bearer " + APPLICATION_TOKEN,
               "Accept":"application/json",
               "Accept-Encoding":"application/json"}
    request = urllib2.Request(url, None, headers)
    result = urllib2.urlopen(request).read()
    r = json.loads(result)
    events = r["events"]
    # Eliminate events that are not within the search radius
    i = 0
    while i < len(events):
        if float(events[i]["distance"]) > radius:
            events.pop(i)
            i -= 1
        i += 1
    # Eliminate events that do not match the eventType
    if eventType != "":
        i = 0
        while i < len(events):
            listedType = events[i]["categories"][1]["name"]
            if listedType != eventType:
                events.pop(i)
                i -= 1
            i += 1
    # Eliminate events that do not match the price
    i = 0
    while i < len(events):
        currencyCode = events[i]["ticketInfo"]["currencyCode"]
        minListedPrice = float(events[i]["ticketInfo"]["minPrice"])
        maxListedPrice = float(events[i]["ticketInfo"]["maxPrice"])
        # To do: convert to US dollars if currency code is different
        if minListedPrice == 0 or maxPrice < minListedPrice or minPrice > maxListedPrice:
            events.pop(i)
            i -= 1
        i += 1
    
    print len(events)
    return events

search("", "44.680239,-68.803044", 100000000, 0, 50, 0, 0)

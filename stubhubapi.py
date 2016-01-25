import urllib2, json

API_URL = "https://api.stubhub.com/search/catalog/events/v3"
APPLICATION_TOKEN = "VsLaqXIQj3mygZTo36tu5rcoxkEa"

def getRates(currencies):
    """
    Finds the exchange rate of currencies to US dollars.
    Args:
        currencies (list): A list of three-letter currency codes.
    Returns:
        dict: A dictionary with currency codes as keys and exchange rates as values.
    """
    currencyString = ""
    for i in currencies:
        currencyString += i + ","
    currencyString = currencyString[:len(currencyString) - 1]
    url = "http://api.fixer.io/latest?base=USD&symbols=" + currencyString
    try:
        result = urllib2.urlopen(url).read()
        rates = json.loads(result)["rates"]
    except:
        rates = {}
        for i in currencies:
            rates[i] = 1.0
    return rates

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

def searchHelper(start, query, coordinates, radius, minPrice, maxPrice, earliestDate, latestDate):
    """
    Return the unfiltered results from the StubHub API that match the given parameters.
    Args:
        start (int): The index of the found results to start at.
        query (str): The query to search for events. If left an empty string, all events are searched.
        coordinates (str): The latitude and longitude, separated by a comma.
        radius (float): The radius around the coordinates to search within, in miles.
        minPrice (float): The minimum price in dollars.
        maxPrice (float): The maximum price in dollars.
        earliestDate (str): The earliest possible UTC time and date, in the form yyyy-mm-dd;hh:mm (24-hour clock).
        latestDate (str): The latest possible UTC time and date, in the form yyyy-mm-dd;hh:mm (24-hour clock).
    Returns:
        dict: A dictionary of the response from the API.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url = API_URL + "?rows=500&status=active"
    url += "&start=" + str(start)
    if query != "":
        url += "&q=" + query
    url += "&point=" + coordinates
    url += "&radius=" + str(radius)
    url += "&fieldList=*,ticketInfo"
    url += "&date=" + earliestDate.replace(";", "T") + "+TO+" + latestDate.replace(";", "T")
    headers = {"Authorization":"Bearer " + APPLICATION_TOKEN,
               "Accept":"application/json",
               "Accept-Encoding":"application/json"}
    request = urllib2.Request(url, None, headers)
    result = urllib2.urlopen(request).read()
    r = json.loads(result)
    return r

def search(query, coordinates, radius, minPrice, maxPrice, earliestDate, latestDate):
    """
    Search the StubHub API for the top events that match the given parameters.
    Args:
        query (str): The query to search for events. If left an empty string, all events are searched.
        coordinates (str): The latitude and longitude, separated by a comma.
        radius (float): The radius around the coordinates to search within, in miles.
        minPrice (float): The minimum price in dollars.
        maxPrice (float): The maximum price in dollars.
        earliestDate (str): The earliest possible UTC time and date, in the form yyyy-mm-dd;hh:mm (24-hour clock).
        latestDate (str): The latest possible UTC time and date, in the form yyyy-mm-dd;hh:mm (24-hour clock).
    Returns:
        list: A list of the JSON responses from events that match the search query.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    # Gets the unfiltered events from the API
    r = searchHelper(0, query.replace(" ", "+"), coordinates, radius, minPrice, maxPrice, earliestDate, latestDate)
    events = r["events"]
    # Eliminate events that are not within the search radius
    i = 0
    while i < len(events):
        if float(events[i]["distance"]) > float(radius):
            events.pop(i)
            i -= 1
        i += 1
    # Eliminate events that do not match the price
    while i < len(events):
        if minListedPrice == 0 or maxPrice < minListedPrice or minPrice > maxListedPrice:
            events.pop(i)
            i -= 1
        i += 1
    # Eliminate events that do not have a description
    i = 0
    while i < len(events):
        if not events[i].has_key("description"):
            events.pop(i)
            i -= 1
        i += 1
    # Returns a list of filtered events
    return events

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
    result = urllib2.urlopen(url).read()
    r = json.loads(result)
    return r["rates"]

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

def search(eventType, coordinates, radius, minPrice, maxPrice, earliestDate, latestDate):
    """
    Search the StubHub API for the top events that match the given parameters.
    Args:
        eventType (str): The broad category of event (Concert, Sports, Theater, or Arts). If none is specified, all events are searched.
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
    url = API_URL + "?rows=500&status=active"
    if eventType != "":
        url += "&q=" + eventType
        if eventType == "Theater" or eventType == "Arts":
            eventType = "Theater tickets and Arts"
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
    otherCurrencies = []
    while i < len(events):
        currencyCode = events[i]["ticketInfo"]["currencyCode"]
        if currencyCode != "USD" and not currencyCode in otherCurrencies:
            otherCurrencies.append(currencyCode)
        i += 1
    rates = getRates(otherCurrencies)
    i = 0
    while i < len(events):
        currencyCode = events[i]["ticketInfo"]["currencyCode"]
        minListedPrice = float(events[i]["ticketInfo"]["minPrice"])
        maxListedPrice = float(events[i]["ticketInfo"]["maxPrice"])
        if currencyCode != "USD":
            minListedPrice = minListedPrice / rates[currencyCode]
            maxListedPrice = maxListedPrice / rates[currencyCode]
        if minListedPrice == 0 or maxPrice < minListedPrice or minPrice > maxListedPrice:
            events.pop(i)
            i -= 1
        i += 1
    print len(events)
    return events

search("", "44.680239,-68.803044", 100000000, 0, 50, "2016-02-01;00:00", "2016-02-02;00:00")

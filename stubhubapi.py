import urllib2, json

url = "https://api.stubhub.com/search/catalog/events/v3"
headers = {"Authorization":"Bearer VsLaqXIQj3mygZTo36tu5rcoxkEa",
           "Accept":"application/json",
           "Accept-Encoding":"application/json"}
request = urllib2.Request(url, None, headers)
result = urllib2.urlopen(request).read()
r = json.loads(result)
print r

import urllib2, json, base64

url = "https://api.stubhub.com/search/catalog/events/v3?status=active&state=NY"
headers = {"Authorization":"Bearer "}
request = urllib2.Request(url, headers)
result = urllib2.urlopen(request).read()
r = json.loads(result)
print r

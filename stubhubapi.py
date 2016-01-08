import urllib2

url = "https://api.stubhub.com/search/catalog/events/v3?status=active&state=NY"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"}
request = urllib2.Request(url, None, headers)
result = urllib2.urlopen(request).read()
print result

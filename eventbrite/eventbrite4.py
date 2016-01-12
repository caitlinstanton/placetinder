import requests
response = requests.get(
    "https://www.evbdev.com/ebapi/v3/users/me/owned_events/",
    headers = {
        "Authorization": "Bearer JYHSYPNUFM546GH2YJSO",
    },
    verify = True,  # Verify SSL certificate
)
print response.json()['events'][0]['name']['text']
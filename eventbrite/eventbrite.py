from eventbrite import Eventbrite
ebrite = Eventbrite('JYHSYPNUFM546GH2YJSO')
user = ebrite.get('/search/events',concerts)

print user
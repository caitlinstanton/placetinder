from eventbrite import Eventbrite

eventbrite = Eventbrite('JYHSYPNUFM546GH2YJSO')

user = eventbrite.get_user()
print user['id']

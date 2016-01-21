from flask import Flask, render_template
from simplejson import loads
import requests
from eventbrite import Eventbrite

app = Flask(__name__)

# eventbrite constants
TEAMS_API_URL = 'https://www.eventbriteapi.com/v3/events/?token={}'
eventbrite = Eventbrite('JYHSYPNUFM546GH2YJSO')

@app.route('/teams/')
def list_teams():
    r = eventbrite.get('https://www.eventbriteapi.com/v3/events/search/?token=JYHSYPNUFM546GH2YJSO&expand=venue')
    print r.content
    teams_data = loads(r.content.description.text)
    return render_template('teams.html', teams = teams_data)

if __name__ == '__main__':
    app.run()

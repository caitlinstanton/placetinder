<h1>placetinder</h1>

<table>
<tr><th>Member</th><th>Role</th></tr>
<tr><td>Caitlin Stanton</td><td>Leader</td></tr>
<tr><td>Vivian Li</td><td>UX</td></tr>
<tr><td>Isaac Gerstein</td><td>Middleware</td></tr> 
<tr><td>Kathy Wang</td><td>Backend</td></tr> 
</table>

<h2>Concept</h2>
<p>Are you bored? Don't know where you wanna go? Come to place tinder!!</p>
<p>Place Tinder helps users find places to go and events to see by selecting random events after the user puts in specifications.</p>

<h2>User Flow</h2>
- User creates an account
- User puts in specifications for what they want to go to:
  - Type of event
  - Price
  - Location (obtained through geolocation), and distance from location
  - Date range
- App generates random results that fit those specifications from all of the APIs
- Results are shown one at a time, and user is given the choice to either reject or attend events
  - Liked events will be added to a to-do list
- Events on the to-do list will have all of the information for the event, including its name, description, date/time, location, and link to the site where you can purchase tickets, book a reservation, etc.

<h2>How to Run</h2>
<b>ONLINE:</b>
Connect to the web app through either <a href="http://placetinder.mooo.com">our site</a> or <a href="http://162.243.17.138">the IP address</a>, create an account or sign in, and see Place Tinder at work!
<b>LOCALLY:</b>
1. Install the following libraries using 'pip install'
  - Flask
  - sqlite3
  - hashlib
  - urllib2
  - json
  - module
  - argparse
  - pprint
  - sys
  - urllib
  - oauth2
  - random
  - requests
2. Run 'python app.py' in your terminal
3. Navigate to 'localhost:8000'
4. Sign in or create an account
5. Experience placetinder!

<h2>Technologies</h2>
- HTML/CSS
- JavaScript
- Python
- APIs:
  - Yelp
  - StubHub
  - Eventbrite
  - Google Maps (for geolocation)
- Hosted on Digital Ocean

<h2>In the Future</h2>
- User can manually add events to to-do list
- More specifications to choose events
- Suggest it to a friend
- Notifications for upcoming events on to-do list (Twilio, Sendgrid)
- Suggested events

<h2>CHANGELOG</h2>
12/21
Created routes and templates
<br>
12/23
User can create an account and log in
<br>
01/06
Used JavaScript to display all future events with Eventbrite
Homepage styling
<br>
01/13
Yelp API completed
Stubhub API completed
Login/create styling
<br>
01/23
Eventbrite API completed
Results displayed
To-do list functionality created
<br>
01/24
Final touches, connected to DigitalOcean and created URL
<br>
01/25
VICTORY!

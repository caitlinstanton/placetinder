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
<p>Check out our demo video <a href="https://youtu.be/HdFZLeQNU0A">here!</a></p>

<h2>User Flow</h2>
<ul>
  <li>User creates an account</li>
  <li>User puts in specifications for what they want to go to:
    <ul>
      <li>Type of event</li>
      <li>Price</li>
      <li>Location (obtained through geolocation), and distance from location</li>
      <li>Date range</li>
    </ul>
  </li>
  <li>App generates random results that fit those specifications from all of the APIs</li>
  <li>Results are shown one at a time, and user is given the choice to either reject or attend events</li>
  <li>Liked events will be added to a to-do list</li>
  <li>Events on the to-do list will have all of the information for the event, including its name, description, date/time, location, and link to the site where you can purchase tickets, book a reservation, etc.</li>
</ul>

<h2>How to Run</h2>
<b>ONLINE:</b>
Connect to the web app through either <a href="http://placetinder.mooo.com">our site</a> or <a href="http://162.243.17.138">the IP address</a>, create an account or sign in, and see Place Tinder at work!
<br><br>
<b>LOCALLY:</b>
<br>
<ol>
  <li>Install the following libraries using 'pip install':
    <ul>
      <li>Flask</li>
      <li>sqlite3</li>
      <li>hashlib</li>
      <li>urllib2</li>
      <li>json</li>
      <li>module</li>
      <li>argparse</li>
      <li>pprint</li>
      <li>sys</li>
      <li>urllib</li>
      <li>oauth2</li>
      <li>random</li>
      <li>requests</li>
    </ul>
  </li>
  <li>Run 'python app.py' in your terminal</li>
  <li>Navigate to 'localhost:8000'</li>
  <li>Sign in or create an account</li>
  <li>Experience placetinder!</li>
</ol>

<h2>Technologies</h2>
<ul>
  <li>HTML/CSS</li>
  <li>JavaScript</li>
  <li>Python</li>
  <li>APIs:
    <li>Yelp</li>
    <li>StubHub</li>
    <li>Eventbrite</li>
    <li>Google Maps (for geolocation)</li>
  </li>
  <li>Hosted on Digital Ocean</li>
</ul>

<h2>In the Future</h2>
<ul>
  <li>User can manually add events to to-do list</li>
  <li>More specifications to choose events</li>
  <li>Suggest it to a friend</li>
  <li>Notifications for upcoming events on to-do list (Twilio, Sendgrid)</li>
  <li>Suggested events</li>
</ul>

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

<h2>Bugs</h2>
- StubHub events are only being displayed when placetinder is run on 'localhost:8000'

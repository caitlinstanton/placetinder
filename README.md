<h1>placetinder</h1>

<table border="1" align="center">
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
- User creates an account (with their email to get notifications?)
- User puts in specifications for what they want to go to:
  - Category of event
  - Price
  - Location (and distance from)
  - Date range
- App generates random results from all of the APIs that fit those specifications
- Results are shown one at a time, and user is given the choice to either swipe left (reject) or swipe right (attend) events, or just skip them entirely
  - Rejected items will not pop up again
  - Liked events will be added to a to-do list (?)
  - Skipped events will stay on the list of results
- Events on the to-do list will lead to the site where you can purchase tickets, book a reservation, etc.

<h2>Technologies</h2>
<strong>Things We Know</strong>
- HTML/CSS
- JavaScript
- Python
<br>
<strong>Things We Can Figure Out</strong>
- Handlebars (or other UX framework)
- APIs:
  - Yelp
  - StubHub
  - Eventbrite
  - Fandago
  - Ticketmaster
  - Google Maps
  - Sendgrid
<br>
<strong>Ehhh</strong>
- Geolocation
- Digital Ocean server thing

<h2>Additional Features</h2>
- Set up a server on Digital Ocean
- User can manually add events to to-do list
- More specifications to choose events
- Show recommendations based on to-do list
- Suggest it to a friend

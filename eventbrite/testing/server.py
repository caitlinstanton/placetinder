from flask import Flask, render_template, request, flash, session, jsonify
from flask.ext.cors import CORS
import eventbrite
import model
import os
import json

from sqlalchemy.orm import class_mapper

app = Flask(__name__)
app.secret_key = "djakljdfgahgfoahufha"

cors = CORS(app)

#

if page > 1:
        return
auth_tokens = {'app_key':  'QYVMDRXBF4JEPEVXQN',
	       'user_key': '1419812832131841160460'}
client = eventbrite.EventbriteClient(auth_tokens)


response = client.event_search({"city":"San Francisco","category":"music", "max": maxresults, "page": page})
rendered_events = []
events = response['events']

for i in range(len(events)):
        if "event" in events[i]:
		event = events[i]["event"]

		row = [event['title'], event['id'],event["status"],event["url"], event['venue']['name'], event["description"]]
		rendered_events.append(row)

		print "\n"
		if "tickets" in event:
			tickets = event["tickets"]
                for j in range(len(tickets)):

			ticket_list = [tickets[j]["ticket"]]
			rendered_events.append(ticket_list)
			print "\n"
        else :
		total_items = events[i]["summary"]["total_items"]
		if (maxresults * page) < total_items:
			next_page = page + 1
                print "NEED TO CALL AGAIN!"
                apicall(page = next_page)
else:
	print "GOT ALL THE STUFF!"
	print rendered_events
	return rendered_events


eventbritecall()

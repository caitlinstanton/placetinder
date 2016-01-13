#import eventbrite

#eventbrite = Eventbrite('JYHSYPNUFM546GH2YJSO')

#user = eventbrite.get_user()
#print user['id']

#!/usr/bin/env python
#! Search Eventbrite for all future events that meet a certain requirement
#! Save the events to a file
#! Make a list of all organizations who created those events
#! Then compile a list of all the events those organizations have in the future

import sys
import eventbrite 
import time
import datetime
import encodings
import xlwt # for dealing with Excel files

# list all the regular fields in the event structure that we want to capture.
parselist=[
    ['title','title'],
    ['start','start_date'],
    ['zone','timezone'],
    ['url','url'],
    #['org dict','organizer'], #this a particularly long field that chokes Excel
    ]
row = 0
#! open a client
eb_auth_tokens = {'app_key': '3G4ETLLKNUFTQNPPKQ'}
eb_client = eventbrite.EventbriteClient(eb_auth_tokens)

#! a few initializations
thispage=1 # for stepping through results pages
organizernameset = set()
organizeridset = set()

#! get ready to log results
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet 1')
now = str(datetime.datetime.today())
logstring='Beginning search on ' + now
sheet.write(row,0,logstring) #row, column
row +=2 #leave a row to insert search results
now = str(datetime.date.today())
wbkfilename='eventbritesearch'+now+'.xls'
wbk.save(wbkfilename)

#first write the irregular fields
sheetcolumn = 0
sheet.write(row,sheetcolumn,'org name')
sheetcolumn +=1
#sheet.write(row,sheetcolumn,'city') # venue not necessarily present
#sheetcolumn +=1
#then step through the regular ones
parseindex = 0
for datum in parselist:
    sheet.write(row,sheetcolumn+parseindex,parselist[parseindex][0])
    parseindex +=1
row +=1
#! Search Eventbrite for all future events that meet a certain requirement

thispage=1
searchkeywords="hackathon"
searchdate="Future"
searchParams = {'keywords': searchkeywords, 'date': searchdate, 'page': thispage}
response = eb_client.search_events(searchParams)

events=response['events']
summary=events[0]['summary']
numevents=summary['total_items']
pagesize=summary['num_showing']
lastpage= int(numevents)//pagesize
if int(numevents)%pagesize != 0: # if there's a remainder, pull one more page
    lastpage +=1
    
del events[0]


while thispage <= lastpage:
    searchParams = {'keywords': searchkeywords, 'date': searchdate, 'page': thispage} # yeah I know I am asking for page 1 twice
    response = eb_client.search_events(searchParams)
    events=response['events']
    del events[0]
    print "Now on page" + str(thispage)
    events=response['events']
    for event in events:
        innerevent=event['event']
        sheetcolumn = 0
        evorganizer=innerevent['organizer']
        organizeridset.add(evorganizer['id'])
        evorganizer=evorganizer['name']
        organizernameset.add(evorganizer)
        sheet.write(row,sheetcolumn,unicode(evorganizer))
        sheetcolumn +=1
#        evcity=innerevent['venue']['city'] #venue not necessarily present. Need to test
#        sheet.write(row,sheetcolumn,unicode(evcity))
#        sheetcolumn +=1
        parseindex = 0
        for datum in parselist:
            key = parselist[parseindex][1]
            sheet.write(row,sheetcolumn+parseindex,unicode(innerevent[key]))
            parseindex +=1
        wbk.save(wbkfilename)
        row +=1     
    thispage += 1

logstring = "We found " + numevents + " events that reference '" + searchkeywords + "' organized by " + str(len(organizernameset)) + " organizers"
row +=1
sheet.write(1,0,logstring)
wbk.save(wbkfilename)
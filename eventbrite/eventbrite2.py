import urllib2,json,codecs,string   #importing necessary libraries
var0="N/A"                          #initialise the variables with any random values
var10="N/A"
var12="N/A"
fob=codecs.open('/Users/Caitlin/Desktop/ram.csv','a','utf-8')     #create and open a csv file with utf-8 encoding format
fob.write("Event_Name,Event_url,City,Address,End_date,Organiser_name,Organiser url,Category_name,Format")  #print the column names
fob.write("\n")
for line in open('/Users/Caitlin/Desktop/input.txt','r').readlines():      #input.txt is a file containing url's one per line,read each line and input the line to urllib,that line must contain oauth token to authenticate
    data=json.load(urllib2.urlopen(line))        #load response in json format
    for item in data['events']:                  #walking through the json data through a for loop
       var1=item['name']['text']                 #var1 is the variable1 containing 'event name' and all the variables follow the order of column names..
       var1=var1.replace(',','')                 #replace any commas with white space in the variable
       var2=item['url']                          #var2 is the variable2 represrenting url of the event
       var3=item['venue']['address']['city']     #var3 gives city in which event will be geld
       var4=item['venue']['address']['address_1'] #var4,var5 contains address of the event in two parts
       if var4 is None:                            #check if there is None case in var3,var4,var5 and if exits replace with N/A
          var4="N/A"
       if var3 is None:
          var3="N/A"
       if var4 is not None:
          var4=var4.replace(',','')                #replace any commas in the address with the space 
       var5=item['venue']['address']['address_2'] 
       if var5 is not None:
          var5=var5.replace(',','')
       if var4 is not None:
           if var5 is not None:
              if var4!=var5:
               var0=var4+var5      #var0 is concatenation of two parts of the addresses if both are not None        
       var6=item['end']['local'].split("T")[0]   #var6 is the variable6 containing end_date of the event
       var7=item['organizer']['name']            #var7 gives the organiser name 
       if var7 is None:                          #if var7 is None replace it with N/A
            var7="N/A"
       if var7 is not None:   
            var7=string.replace(var7,',',' ')     #replace commas with space in the replace function
       var8=item['organizer']['url']               #var8 gives the organiser url
       var8=var8.replace(","," ")            
       var9=item['category']                        #var10 gives the category name
       if var9 is not None:
          var10=item['category']['name']           #var12 gives the format name
       var10=string.replace(var10,","," ")   
       var11=item['format']
       if var11 is not None:
           var12= item['format']['name']
       var12=string.replace(var12,',',' ',9)         
       if var4==var5:   #There are two cases in address field if they are same the write the following output to the output file saperated with commas which is required for a csv file
          fob.write(var1+","+var2+","+var3+","+var0+","+var6+","+var7+","+var8+","+var10+","+var12)
          fob.write("\n")
       else:    
          fob.write(var1+","+var2+","+var3+","+var4+","+var6+","+var7+","+var8+","+var10+","+var12)
          fob.write("\n")
fob.close()        #close the file 
import time
from socket import *
import datetime
from datetime import date
import calendar

#create a date object
todaydate = date.today()
#create a time object
now = datetime.datetime.utcnow()
#makes the english translation of the day
dayOfWeek = calendar.day_name[todaydate.weekday()]

if dayOfWeek == "Sunday":
    dayOfWeek = "U"
if dayOfWeek == "Monday":
    dayOfWeek = "M" 
if dayOfWeek == "Tuesday":
    dayOfWeek = "T"
if dayOfWeek == "Wednesday":
    dayOfWeek = "W"
if dayOfWeek == "Thursday":
    dayOfWeek = "R"
if dayOfWeek == "Friday":
    dayOfWeek = "F"
if dayOfWeek == "Saturday":
    dayOfWeek = "S"

pings = 1
while pings < 11:
    serverName = '127.0.0.1'
    serverPort = 12000
    serverAddress = (serverName,serverPort)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = "Ping" + " " + str(pings) + " " + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + " " + dayOfWeek + " " + str("{:%H:%M}".format(now)) + " UTC"
    print(message)
    #timeout set to 1sec
    clientSocket.settimeout(1)
    begin = time.time()
    #send byte encoded message 
    clientSocket.sendto(message.encode(),serverAddress)
    
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        #decodes from byte code
        print (bytes.decode(modifiedMessage))
        end = time.time()
        #formats elapsed time to 4 digits to 3 dec place precision
        endToEnd = "{:4.3f}".format(end-begin)
        print("RTT:",endToEnd)
    except timeout:
        print ('Request timed out')
    pings = pings + 1

clientSocket.close()


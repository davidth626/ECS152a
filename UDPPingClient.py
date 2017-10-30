import time
from socket import *
import datetime
from datetime import date
import calendar

current_time = datetime.datetime.utcnow()
todaydate = date.today()
now = datetime.datetime.utcnow()
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
    message = "Ping" + " " + str(pings) + " " + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + " " + dayOfWeek + " " + str("{:%H:%M}".format(current_time)) + " UTC"
    print(message)
    clientSocket.settimeout(1)
    begin = time.time()
    clientSocket.sendto(message.encode(),serverAddress)
    
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        print(modifiedMessage)
        end = time.time()
        endToEnd = "{:4.3f}".format(end-begin)
        print("RTT:",endToEnd)
    except timeout:
        print ('Request timed out')
    pings = pings + 1

clientSocket.close()


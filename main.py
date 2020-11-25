import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import schedule
import time
import join
import info
import timeTable

driver =  webdriver.Chrome('C:\\web driver\\chromedriver.exe')
e = datetime.datetime.now()

day = (e.strftime("%a"))
print(day)

if day=="Mon":
    monday()
elif day=="Tue":
    tuesday() 
elif day=="Wed":
    wednesday()
elif day=="Thu":
    thursday()
elif day=="Fri":
    friday()
elif day=="Sat":
    saturday()
else:
    print("Its sunday")




def monday():
    schedule.every().monday.at(firstClass).do(joinChem)
    schedule.every().monday.at(secondClass).do(joinEnglish)
    schedule.every().monday.at(thirdClass).do(joinPhysics)
    schedule.every().monday.at(fourthClass).do(joinComputer)
    schedule.every().monday.at(fifthClass).do(joinMaths)

def tuesday():
    schedule.every().tuesday.at(firstClass).do(joinChem)
    schedule.every().tuesday.at(secondClass).do(joinEnglish)
    schedule.every().tuesday.at(thirdClass).do(joinPhysics)
    schedule.every().tuesday.at(fourthClass).do(joinComputer)
    schedule.every().tuesday.at(fifthClass).do(joinMaths)

def wednesday():
    schedule.every().wednesday.at(firstClass).do(joinChem)
    schedule.every().wednesday.at(secondClass).do(joinEnglish)
    schedule.every().wednesday.at(thirdlass).do(joinPhysics)
    schedule.every().wednesday.at(fourthClass).do(joinComputer)
    schedule.every().wednesday.at(fifthClass).do(joinMaths)

def thursday():
    schedule.every().thursday.at(firstClass).do(joinChem)
    schedule.every().thursday.at(secondClass).do(joinEnglish)
    schedule.every().thursday.at(thirdClass).do(joinPhysics)
    schedule.every().thursday.at(fourthClass).do(joinComputer)
    schedule.every().thursday.at(fifthClass).do(joinMaths)

def friday():
    schedule.every().friday.at(firstClass).do(joinChem)
    schedule.every().friday.at(secondClass).do(joinEnglish)
    schedule.every().friday.at(thirdClass).do(joinPhysics)
    schedule.every().friday.at(fourthClass).do(joinComputer)
    schedule.every().friday.at(fifthClass).do(joinMaths)

def saturday():
    schedule.every().saturday.at(firstClass).do(joinChem)
    schedule.every().saturday.at(secondClass).do(joinEnglish)
    schedule.every().saturday.at(thirdClass).do(joinPhysics)
    schedule.every().saturday.at(fourthClass).do(joinComputer)
    schedule.every().saturday.at(fifthClass).do(joinMaths)


while True:
    schedule.run_pending()
    time.sleep(60)
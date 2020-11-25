import info
import timeTable
import time

def joinChem():
    driver.get(chemistry)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinEnglish():
    driver.get(english)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinPhysics():
    driver.get(physics)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinComputer():
    driver.get(computer)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinMaths():
    driver.get(maths)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()


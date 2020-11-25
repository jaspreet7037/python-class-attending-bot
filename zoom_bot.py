from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import keyboard

class zoom_bot:
	def join(self,meeting_link):
		self.bot = webdriver.Chrome("chromedriver.exe")
		self.bot.get(meeting_link)
		time.sleep(3)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)
		time.sleep(10)

		self.bot.quit()

link = open("https://us04web.zoom.us/j/6695688188?pwd=U29KZllZVHdVU1NvT3RhTDQ4dk5BUT09")

obj = zoom_bot()
obj.join(link)
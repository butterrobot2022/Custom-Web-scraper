import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyttsx3
engine = pyttsx3.init()

email = "motingwetlotlo@yahoo.com"
password = "Shadow2003!"
forex_factory_url = "https://www.forexfactory.com/"
chrome_driver = "/Users/motin/Desktop/chromedriver"

engine.say("Good morning, Mr Motingwe. I hope you had a good night's rest!")
engine.runAndWait()
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get(url=forex_factory_url)

driver.execute_script("window.scrollTo(0, 200)")
news = driver.find_element(By.CLASS_NAME, "calendar__table").text.strip("Date").replace("Currency", "").replace("Impact", "").replace("Detail", "").replace("Actual", "").replace("Forecast", "").replace("Previous", "").replace("Graph", "")

engine.say("The following is the table data for today's news events:")
engine.say(news)
engine.runAndWait()

driver.execute_script("window.scrollTo(0, 700)")
latest_news = driver.find_element(By.CLASS_NAME, "news").text.strip("More").replace("Stream", "")
engine.say("The following are the latest news-headlines for the day:")
engine.say(latest_news)
engine.runAndWait()

engine.say("That's all there is for today sir. Happy trading!")
engine.runAndWait()





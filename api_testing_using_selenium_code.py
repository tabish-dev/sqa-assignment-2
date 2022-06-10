# Wikipedia (Search API) testing using Selenium framework

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox()
browser.set_window_size(1100,1100)
browser.set_window_position(0,0)
sleep(1)

browser.get("https://en.wikipedia.org/wiki/Main_Page")
browser.find_element_by_id("searchInput").send_keys("The Nun (2018 film)")
sleep(3)

browser.find_element_by_id("searchInput").send_keys(Keys.RETURN)
sleep(10)

browser.execute_script("window.scrollTo(0,1100);")
sleep(3)

browser.execute_script("window.scrollTo(0,-1100);")
sleep(6)

browser.close()

print("testing has been completed")

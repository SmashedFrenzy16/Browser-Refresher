from selenium import webdriver
import time

browser = webdriver.Chrome() # Change Chrome to Firefox, Edge, Ie or Safari, depending on what browser you want (NOTE: it has to also be installed on your computer for the browser to open)

browser.get(input("Enter in the url you want to navigate to: "))

delay = input("Enter how many seconds you want to wait for between each refresh: ")

while True:

    browser.refresh()

    time.sleep(int(delay))

browser.quit()

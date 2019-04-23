from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import codecs
import os
import time
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path="/Users/jiang/Desktop/ECON900_PS1/ECON900_PS1/html_files/chromedriver", chrome_options=option)
# for i in range(500):
for i in range(1,1065):
	browser.get("https://boardgamegeek.com/browse/boardgame/page/"+str(i))

	completeName = os.path.join("output/", "gamepage"+str(i))
	file_object = codecs.open(completeName, "w", "utf-8")
	html = browser.page_source
	file_object.write(html)
	time.sleep(6)

browser.quit()

# timeout = 20

# list_price = browser.find_elements_by_xpath("//a[@class='add']")
# titles = [x.text for x in list_price]
# print('TITLES:')
# print(titles, '\n')

# game_price = browser.find_elements_by_xpath("//div[@class='aad']")
# prices = [x.text for x in game_price] # same concept as for-loop/ list-comprehension above.
# print("PRICE:")
# print(prices, '\n')


#
#
#   Collect Recipies for Drink Bot
#
#   Description: Scrape the website cocktailbuilder.com for cocktail recipes after inputting ingredients from a json.
#               Will be done from a rasberry pi, and provide the recipes as options on a TFT screen to select as an option.
#
#   Author: Christopher Medrano
#
#   Date Created: 7/13/19
#
#   Last Update: 7/13/19
#

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

# in rasberry pi
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

f = open("ingredients.json")
ing_file = json.load(f)
ingredients = ing_file['ingredients']

driver = webdriver.Chrome()
driver.get("www.cocktailbuilder.com")

print(driver.title)

for ingredient in ingredients:
    elem = driver.find_element_by_id("addingredient")
    elem.send_keys(ingredient)
    elem.send_keys(Keys.RETURN)

driver.close()

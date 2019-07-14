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

# Collect available ingredients
f = open("ingredients.json")
ing_file = json.load(f)
ingredients = ing_file['ingredients']

# Open website
driver = webdriver.Chrome()
driver.get("https://www.cocktailbuilder.com/")

assert driver.title == "Cocktail Builder: Mixed Drinks From What You Already Have"

# counter for ingredients added
i = 0
for ingredient in ingredients:
    add_ingredient = driver.find_element_by_id("addIngredient")
    add_ingredient.send_keys(ingredient)
    found_ingredients = driver.find_elements_by_class_name('tt-suggestion')
    found_ingredients[0].click()
    i = i + 1
    if i == 5:
        driver.find_element_by_class_name("noThanks").find_element_by_tag_name("button").click()

#driver.close()

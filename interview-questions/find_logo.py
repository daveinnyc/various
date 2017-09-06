import re

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://testCompany.com" 
LOGO_URL = "https://cdn.testCompany.com/static/1DBa8k/images/frontend/onboarding/testCompany-small-orange-logo.png"

regex_parens = re.compile('\((.*?)\)')

def get_firefox_browser():
    driver = webdriver.Firefox()
    driver.set_window_size(1200,900)

    return driver


def value_in_parens(string_with_parens):
    # Returns an unquoted inner value
    m = re.search(regex_parens, string_with_parens)
    inner_string = m.group(1)
    inner_string = inner_string.strip('"')
    inner_string = inner_string.strip("'")

    return inner_string


def test_check_for_logo(driver):
    try:
        css_background = browser.find_element_by_css_selector("div.header__logo").value_of_css_property("background-image")
        css_background = value_in_parens(css_background)
    except NoSuchElementException:
        return False

    return css_background 


browser = get_firefox_browser()
browser.get(BASE_URL)

assert test_check_for_logo(browser) == LOGO_URL

browser.close()
print("DONE")

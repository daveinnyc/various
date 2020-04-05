''' 
Task:
 -- Automate 5 test cases against https://hub.docker.com/
 --- Req.1   Must use FF or Chrome
 --- Req.2   At least one signup case
 --- Req.3   At least one login case
 --- Req.4   At least one search related case
 --- Req.5   Comment or docstring for each test

For Req. 3 The known account password was emailed. Update it below 
           at line 30 
For Req. 5 #comments are explanatory for the coding challenge
           'comments are for test documentation


  While developing the following are useful one liners. Assumes not closing 
  firefox explicitly while working on a particular test:

  -- find and kill any running firefoxes, execute all tests
  FFS=$(ps -e |grep firefox|cut -d" " -f1) ; if [ ${#FFS} -ne 0 ] ; \
  then killall firefox ; fi ; py.test -q -s selenium-docker-test.py


  -- find and kill any running firefoxes, execute only 'test_login'
  FFS=$(ps -e |grep firefox|cut -d" " -f1) ;if [ ${#FFS} -ne 0 ] ; \
  then killall firefox ; fi ; py.test -q -s selenium-docker-test.py::test_login


Author: Dave Cuthbert
Copyright: 2016
License: MIT
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random 
import time
import pytest


# GLOBALS
BASE_URL = "https://hub.docker.com" 
KNOWN_ACCOUNT_PWD = ""#Emailed to recruiter


# REQ.1 -- USES FIREFOX
@pytest.fixture
def driver():
    ''' Setup Firefox browser'''
    d = webdriver.Firefox()
    d.set_window_size(1200,900)
    return d


def create_user_id():
    '''Create a (probably) unique id and email based on a known string'''
    random.seed()
    unique_element = random.getrandbits(30)
    common_element = 'ikjuyhwsed'
    return common_element + str(unique_element)


#TESTS BELOW HERE
def test_check_proper_site(driver):
    ''' Verify this is the Docker site before continuing tests.
        Work around to check on the page since no <title> element '''
    driver.get(BASE_URL)
    footer =  driver.find_element_by_class_name("Welcome__footerCopy___3AswA")
    assert "Docker Inc." in  footer.text
    driver.close()


# REQ.2 -- SIGNUP CASE
# This test doesn't verify E2E signup flow since that requires a unique id and
#    a unique email for each account. Instead it only sets up part of the flow
#    to verify page elements and omits the confirmation email
def test_sign_up(driver):
    ''' Verify sign up submission '''
    URL = BASE_URL
    driver.get(URL)

    ACCOUNT_NAME = create_user_id()
    ACCOUNT_PWD = '111' + ACCOUNT_NAME + '$234'
    ACCOUNT_EMAIL = ACCOUNT_NAME + '@gmail.com'

    username = driver.find_element_by_css_selector(
                                "input[placeholder='Choose a Docker Hub ID']")
    username.send_keys(ACCOUNT_NAME)
    password = driver.find_element_by_css_selector(
                                "input[placeholder='Choose a password']")
    password.send_keys(ACCOUNT_PWD)
    email = driver.find_element_by_css_selector(
                                "input[placeholder='Enter your email address']")
    email.send_keys(ACCOUNT_EMAIL)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()
    driver.implicitly_wait(5)

    #Verify sign up confirmation message is returned after click
    confirm_message = driver.find_element_by_xpath(
                                              "//*[contains(text(), 'Sweet!')]")
    assert "Sweet! You're almost ready to go!" in confirm_message.text

    driver.close()



# REQ.3 -- LOGIN CASES
# 3.1 -- successful login 
# This test uses a pre-existing account rather than relying on the output of the
#    earlier test for setup to preserve test independance
def test_login(driver):
    ''' Verfiy login on known user '''
    URL = BASE_URL + "/login"
    driver.get(URL)

    ACCOUNT_NAME = "bobtedcarolalice1"
    ACCOUNT_PWD = KNOWN_ACCOUNT_PWD

    username = driver.find_element_by_css_selector(
                                          "input[placeholder='Username']")
    username.send_keys(ACCOUNT_NAME)
    password = driver.find_element_by_css_selector(
                                          "input[placeholder='Password']")
    password.send_keys(ACCOUNT_PWD)

    submit_button = driver.find_element_by_css_selector(
                                           "button[type='submit']")
    submit_button.click()
    driver.implicitly_wait(5)

    #Verify sign up confirmation message is returned after click
    confirm_message = driver.find_element_by_xpath(
                               "//*[contains(text(), 'Welcome to Docker Hub')]")
    assert "Welcome to Docker Hub" in confirm_message.text

    driver.close()

# 3.2 -- failed login
def test_login_failed(driver):
    ''' Verfiy error message on login failure '''
    URL = BASE_URL + "/login"
    driver.get(URL)

    ACCOUNT_NAME = "bobtedcarolalice1"
    ACCOUNT_PWD = "bad_password"

    username = driver.find_element_by_css_selector(
                                          "input[placeholder='Username']")
    username.send_keys(ACCOUNT_NAME)
    password = driver.find_element_by_css_selector(
                                          "input[placeholder='Password']")
    password.send_keys(ACCOUNT_PWD)

    submit_button = driver.find_element_by_css_selector(
                                          "button[type='submit']")
    submit_button.click()
    driver.implicitly_wait(5)

    #Verify sign up confirmation message is returned after click
    confirm_message = driver.find_element_by_css_selector("p.alert-box")
    assert "Login Failed." in confirm_message.text

    driver.close()



# Req.4 SEARCH TEST
# Search for a known docker container and verify it is returned as expected
def test_search(driver):
    ''' Verfiy basic search functionality '''
    URL = BASE_URL + "/login"
    driver.get(URL)

    ACCOUNT_NAME = "bobtedcarolalice1"
    ACCOUNT_PWD = KNOWN_ACCOUNT_PWD

    #Login -- Normally login code would be extracted to a library function  
    #         rather than repeated in multiple tests
    username = driver.find_element_by_css_selector(
                                          "input[placeholder='Username']")
    username.send_keys(ACCOUNT_NAME)
    password = driver.find_element_by_css_selector(
                                          "input[placeholder='Password']")
    password.send_keys(ACCOUNT_PWD)

    submit_button = driver.find_element_by_css_selector(
                                           "button[type='submit']")
    submit_button.click()

    #Search for the official java container
    # The Search Elementreloads during page rendering so the reference is lost
    #    if it is found too early. Force a hard delay to give page time to 
    #    render fully rather than rely on driver.implicit_wait() which gets 
    #    earlier rendering. Production code woudl use a better method.
    time.sleep(10)
    search_box = driver.find_element_by_css_selector(
                                        "input.SearchBar__searchInput___34nC3")
    search_box.send_keys('Java')
    search_box.send_keys(Keys.RETURN)
    
    #Verify search returns expected docker container
    driver.implicitly_wait(5)
    search_result = driver.find_element_by_css_selector(
                                     "div.RepositoryListItem__repoName___28cOR")
    assert "java" in search_result.text
   
    driver.close()


#EOF

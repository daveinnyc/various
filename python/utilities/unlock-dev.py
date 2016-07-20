''' Short script to get the list of locked companies and unlock them.
    NB: The user password has to be updated before running the script
    
    Author: Dave Cuthbert
    Copyright: 2016
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

#GLOBALS
BASE_URL='INSERT TEST SERVER NAME HERE'
USER='INSERT TEST USER NAME HERE'
PWD='NEED TO UPDATE PASSWORD BEFORE RUNNING THIS SCRIPT'

@pytest.fixture
def driver():
    d = webdriver.Firefox()
    d.set_window_size(1200, 800)
    
    return d
    
def test_login(driver):
    URL=BASE_URL + '/login'
    driver.get(URL)
    
    #LOGIN
    username = driver.find_element_by_css_selector("input[name='userEmail']")
    username.send_keys(USER)
    password = driver.find_element_by_css_selector("input[name='password']")
    password.send_keys(PWD)
    #password.send_keys(Keys.ENTER)
    login_button = driver.find_element_by_id('login-submit-loginpage')
    login_button.send_keys(Keys.ENTER)
    
    #GO TO ADMIN SITE
    driver.implicitly_wait(10)
    admin_link = driver.find_element_by_link_text("Admin Site")
    admin_link.click()
    
    #GO TO LOCKED COMPANIES LIST
    driver.implicitly_wait(10)
    locked_companies = driver.find_element_by_link_text("Locked Companies")
    locked_companies.click()
    
    #GET LIST OF LOCKED COMPANIES
    driver.implicitly_wait(10)
    company_ids = driver.find_elements_by_css_selector('a.unlock')
    while(len(company_ids) != 0):
        company_id = company_ids[0].get_attribute('data-id')
        CSS = 'a.unlock[data-id="{}"]'.format(company_id)
        unlock_me = driver.find_element_by_css_selector(CSS)
        unlock_me.click()
        
        #FILL OUT UNLOCK MODAL
        time_select = driver.find_element_by_css_selector(
                                        "select[name='hours'] [value='72']")
        time_select.click()
        comment_box = driver.find_element_by_css_selector(
                                             "textarea[name='comment']")
        comment_box.send_keys('Auto unlocked')
        unlock_button = driver.find_element_by_css_selector('button')
        unlock_button.click()       
           
        #GET A NEW LIST
        #  Page refreshes as old items disappear causing links to go stale
        #  Adding a hard sleep fixes the issue but costs 4 min for 80 item list
        time.sleep(5)
        company_ids = driver.find_elements_by_css_selector('a.unlock')
    #driver.close()
    
#EOF


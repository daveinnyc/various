from selenium import webdriver

# Workaround for configuration issue in test environment
# Reset data for testing


# Create a broswer to test with
browser = webdriver.Firefox()

# Go to dev.workmarket.com
browser.get("https://dev.workmarket.com")
assert "Freelance Management System" in browser.title

# Go to login page
log_in_button = browser.find_element_by_css_selector("li.log-in a:nth-child(1)")
log_in_button.click()
assert "Log In" in browser.title

# Login
user_name_field = browser.find_element_by_id("inputEmail4")
user_name_field.send_keys("PUT_USR_HERE")
user_password_field = browser.find_element_by_id("inputPassword4")
user_password_field.send_keys("PUT_PWD_HERE")
submit_credentials_log_in_button = browser.find_element_by_id("login-submit-loginpage")
submit_credentials_log_in_button.click()

# Go to admin page
admin_page_link = browser.find_element_by_link_text("Admin Site")
admin_page_link.click()

# Find locked accounts
# List redraws so need to give page a chance to catch up to script
locked_accounts_link = browser.find_element_by_link_text("Locked Companies")
locked_accounts_link.click()
browser.implicitly_wait(5)              #SLEEP 
locked_account_table = browser.find_element_by_id("companies_list")
account_table_rows = locked_account_table.find_elements_by_tag_name("tr")
for r in account_table_rows:
    cells = r.find_elements_by_tag_name("td")
    print "cells: " + cells
    print "C[0]: " + cells[0]
    print "C[1]: " + cells[1]



# browser.close()
# EOF

import pytest
import ../__init__ as init
from selenium import webdriver

LOCAL_INSTANCE =  "127.0.0.1:5000"


def test_is_running():
    init.is_running()
    
    # Firefox 
    driver = webdriver.Firefox()
    driver.get(LOCAl_INSTANCE)
    
    assert driver.body == "Flask is running"
    
    
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setup")
def test_open_website(setup):
    
    driver = setup

    # Go to the Magento site
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    # Find and print the site title
    print("Page Title:", driver.title)
    
    # Try to find a basic element
    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("top")
    time.sleep(5)
    #wait = WebDriverWait(10)
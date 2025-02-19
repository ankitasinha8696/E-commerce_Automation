from selenium import webdriver
import pytest
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():

    #service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")  
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--ignore-ssl-errors=yes")
    chrome_options.add_argument("--ignore-certificate-errors-spki-list")
    chrome_options.add_argument("--no-sandbox")  # For Linux environments
    chrome_options.add_argument("--disable-dev-shm-usage") 

    #service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options)
    

    # Close the browser
    yield driver
    driver.quit()
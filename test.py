from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Go to the Magento site
    driver.get("https://magento.softwaretestingboard.com/")
    
    # Find and print the site title
    print("Page Title:", driver.title)
    
    # Try to find a basic element
    search_box = driver.find_element(By.ID, "search")
    print("Search box found successfully!")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser
    driver.quit()
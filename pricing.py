
from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize Chrome WebDriver (replace with your desired browser)
driver = webdriver.Chrome()
site = driver.get("https://www.amazon.in/")

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("samsung")
driver.find_element(By.ID, 'nav-search-submit-button').click()
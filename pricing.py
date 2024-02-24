
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
website_urls = [
   "https://www.flipkart.com/",
 "https://www.amazon.in/",
 "https://www.ebay.com/",
"https://www.myntra.com/"
] 

product = "iphone"

search_selectors = {
    "https://www.flipkart.com/": By.CLASS_NAME, "Pke_EE"
    "https://www.amazon.in/": By.ID, "twotabsearchtextbox"
    "https://www.ebay.com/" : By.CLASS_NAME, "gh-tb ui-autocomplete-input"
    "https://www.myntra.com/": By.CLASS_NAME, "desktop-searchBar"
}

submit_selectors = {
    "https://www.flipkart.com/": By.CLASS_NAME, "_2iLD__ "
    "https://www.amazon.in/": By.ID, "nav-search-submit-button"
    "https://www.ebay.com/" : By.ID, "gh-btn"
    "https://www.myntra.com/": By.CLASS_NAME, "desktop-submit"
}


# Initialize Chrome WebDriver (replace with your desired browser)
driver = webdriver.Chrome()
for url in website_urls:
    driver.get(url)
    search_element = driver.find_element(search_selectors[url])
    search_element.send_keys(product)
    search_element.send_keys(Keys.ENTER)  



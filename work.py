from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
website_urls = [
     "https://www.flipkart.com/",
    "https://www.amazon.in/",
     "https://www.ebay.com/",
     "https://www.myntra.com/"
]
search_selectors = {
    "https://www.flipkart.com/": [By.CLASS_NAME, "Pke_EE"],
    "https://www.amazon.in/": [By.ID, "twotabsearchtextbox"],
    "https://www.ebay.com/" : [By.ID, "gh-ac"],
    "https://www.myntra.com/": [By.CLASS_NAME, "desktop-searchBar"]
}

submit_selectors = {
    "https://www.flipkart.com/": [By.CLASS_NAME, "_2iLD__ "],
    "https://www.amazon.in/": [By.ID, "nav-search-submit-button"],
    "https://www.ebay.com/" : [By.ID, "gh-btn"],
    "https://www.myntra.com/": [By.CLASS_NAME, "desktop-submit"]
}
product = "iPhone 14"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Initialize variables to store best price and product details
best_price = None
best_product_details = None

for url in website_urls:
    driver.get(url)

    # Find and interact with search element using selector from dictionary
    search_element = driver.find_element(search_selectors[url][0], search_selectors[url][1])
    search_element.send_keys(product)
    search_element.send_keys(Keys.ENTER)
    
     #Extraction 
    names = driver.find_elements(By.XPATH ,"//span[@class='a-size-medium a-color-base a-text-normal']")
    prices = driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")
    for name,price in zip(names,prices) :
        if product in name.text:
            print(name.text, price.text)
            sleep(2)
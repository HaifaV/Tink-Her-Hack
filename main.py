from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
website_urls = [
    # "https://www.flipkart.com/",
    "https://www.amazon.in/",
    # "https://www.ebay.com/",
    # "https://www.myntra.com/"
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
    
    for x in range(3, 1000):
        try:
            product1 = driver.find_element(By.XPATH, f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{x}]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span')
            price1 = driver.find_element(By.XPATH, f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{x}]/div/div/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/a/span/span[2]/span[2]')
        except NoSuchElementException:
            print("No Such Element Found")
            sleep(2)
        else:
            print(product1.text, price1.text)
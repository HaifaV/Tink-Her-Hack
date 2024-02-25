from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

best_price = None
best_product_details = None

website_urls = [
     "https://www.flipkart.com/",
     "https://www.amazon.in/",
     "https://www.ebay.com/",
   
]
search_selectors = {
    "https://www.flipkart.com/": [By.CLASS_NAME, "Pke_EE"],
    "https://www.amazon.in/": [By.ID, "twotabsearchtextbox"],
    "https://www.ebay.com/" : [By.ID, "gh-ac"],
}

submit_selectors = {
    "https://www.flipkart.com/": [By.CLASS_NAME, "_2iLD__ "],
    "https://www.amazon.in/": [By.ID, "nav-search-submit-button"],
    "https://www.ebay.com/" : [By.ID, "gh-btn"],
}

extract_name_selectors = {
    "https://www.flipkart.com/": [By.XPATH, "//div[@class='_4rR01T']"],
    "https://www.amazon.in/": [By.XPATH , "//span[@class='a-size-medium a-color-base a-text-normal']"],
    "https://www.ebay.com/" : [By.XPATH,  "//span[@role='heading']"],
}

extract_price_selectors = {
    "https://www.flipkart.com/": [By.XPATH, "//div[@class='_30jeq3 _1_WHN1']"],
    "https://www.amazon.in/": [By.XPATH,"//span[@class='a-price-whole']"],
    "https://www.ebay.com/" : [By.XPATH,"//span[@class='s-item__price']"],
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
    try :
         names = driver.find_elements(extract_name_selectors[url][0],extract_name_selectors[url][1])
         prices = driver.find_elements(extract_price_selectors[url][0],extract_price_selectors[url][1])
         print(url)
         for name,price in zip(names,prices) :
              if product in name.text:
                  current_price = float(price.text.replace(",", ""))  # Convert price to float
                  if best_price is None or current_price < best_price:
                    best_price = current_price
                    best_product_details = (name.text, price.text, url)
    except NoSuchElementException:
        pass  # Continue to the next website if elements are not found

driver.quit()

if best_product_details:
    print("Product with the lowest price:")
    print("- Name:", best_product_details[0])
    print("- Price:", best_product_details[1])
    print("- Website:", best_product_details[2])
else:
    print("Product not found on any of the websites.")
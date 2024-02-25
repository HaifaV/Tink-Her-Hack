from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import re  # Import regular expressions module

# Dummy function for currency conversion - you'll need to replace this with a real implementation
def convert_currency_to_inr(amount, currency):
    # Placeholder for currency conversion logic
    # This should call a currency conversion API to get the real conversion rate
    # For the sake of example, let's assume 1 USD = 75 INR
    conversion_rates = {'USD': 75}
    return amount * conversion_rates.get(currency, 1)

def clean_and_convert_price(price_str):
    # Detect currency
    currency = 'INR'
    if '$' in price_str:
        currency = 'USD'
    # More currency symbols can be added here

    # Attempt to clean the price string by removing non-numeric characters except the decimal point
    # and splitting by non-numeric characters to handle cases where multiple prices are concatenated
    cleaned_price_parts = re.split(r'[^\d.]+', price_str)

    # Filter out empty strings and convert to float, taking the first valid price
    cleaned_prices = [float(part) for part in cleaned_price_parts if part]
    if not cleaned_prices:
        raise ValueError(f"Could not extract any prices from the string: {price_str}")
    price = cleaned_prices[0]  # Assuming the first price is the relevant one

    # Convert to INR if necessary
    if currency != 'INR':
        price = convert_currency_to_inr(price, currency)
    
    return price


website_urls = [
    "https://www.flipkart.com/",
    "https://www.amazon.in/",
    "https://www.ebay.com/",
]

search_selectors = {
    "https://www.flipkart.com/": [By.CLASS_NAME, "Pke_EE"],
    "https://www.amazon.in/": [By.ID, "twotabsearchtextbox"],
    "https://www.ebay.com/": [By.ID, "gh-ac"],
}

submit_selectors = {
    "https://www.flipkart.com/": [By.CLASS_NAME, "_2iLD__ "],
    "https://www.amazon.in/": [By.ID, "nav-search-submit-button"],
    "https://www.ebay.com/": [By.ID, "gh-btn"],
}

extract_name_selectors = {
    "https://www.flipkart.com/": [By.XPATH, "//div[@class='_4rR01T']"],
    "https://www.amazon.in/": [By.XPATH , "//span[@class='a-size-medium a-color-base a-text-normal']"],
    "https://www.ebay.com/": [By.XPATH, "//span[@role='heading']"],
}

extract_price_selectors = {
    "https://www.flipkart.com/": [By.XPATH, "//div[@class='_30jeq3 _1_WHN1']"],
    "https://www.amazon.in/": [By.XPATH, "//span[@class='a-price-whole']"],
    "https://www.ebay.com/": [By.XPATH, "//span[@class='s-item__price']"],
}

product = "iPhone 14"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

best_price = None
best_product_details = None

for url in website_urls:
    driver.get(url)

    # Find and interact with search element using selector from dictionary
    search_element = driver.find_element(search_selectors[url][0], search_selectors[url][1])
    search_element.send_keys(product)
    search_element.send_keys(Keys.ENTER)
    
    try:
        names = driver.find_elements(extract_name_selectors[url][0], extract_name_selectors[url][1])
        prices = driver.find_elements(extract_price_selectors[url][0], extract_price_selectors[url][1])

        for name, price_element in zip(names, prices):
            if product.lower() in name.text.lower():
                price_text = price_element.text
                current_price = clean_and_convert_price(price_text)  # Clean and convert the price

                if best_price is None or current_price < best_price:
                    best_price = current_price
                    best_product_details = (name.text, price_text, url)
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

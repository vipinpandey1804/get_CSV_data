from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def download_commodity_data(commodity_name, username, password):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the website
        driver.get("https://www.investing.com/commodities/copper-historical-data")  # Replace with appropriate URL

        # Click the sign-in link
        sign_in_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/header/div[1]/section/div[3]/ul/li[1]/button/span'))
        )
        sign_in_link.click()

        # Click the email sign-in option
        email_sign_in = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/form/button[3]/span'))
        )
        email_sign_in.click()

        # Fill in login credentials
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/form/div[3]/input'))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/form/div[5]/input'))
        )
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Wait for the page to load and the "Download Data" button to appear
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Download Data"))
        )

        # Click the "Download Data" button
        download_button.click()

        # Wait for the download to complete (adjust the time if needed)
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred for {commodity_name}: {e}")

    finally:
        driver.quit()

# Usage example
commodities = [
    {"name": "Gold", "username": "replicablockchain@gmail.com", "password": "Qwerty@123"},
    {"name": "Copper", "username": "replicablockchain@gmail.com", "password": "Qwerty@123"},
    {"name": "Silver", "username": "replicablockchain@gmail.com", "password": "Qwerty@123"},
    
]

for commodity in commodities:
    download_commodity_data(commodity["name"], commodity["username"], commodity["password"])

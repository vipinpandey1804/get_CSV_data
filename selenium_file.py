from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

# Set up the Chrome driver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://www.investing.com/commodities/copper-historical-data")
# 'https://www.investing.com/commodities/gold-historical-data'
# 'https://www.investing.com/commodities/silver-historical-data'

try:

    # Wait for the sign-in link to appear and click it
    sign_in_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/header/div[1]/section/div[3]/ul/li[1]/button/span'))
    )
    sign_in_link.click()
    print("sign_in_link Execute!!")
    
    email_sign_in = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/form/button[3]'))
    )
    email_sign_in.click()
    print("email_sign_in Execute!!")


    # Wait for the login form to appear and fill in your credentials
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/form/div[3]/input'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/form/div[5]/input'))
    )

    username_field.send_keys("replicablockchain@gmail.com")
    password_field.send_keys("Qwerty@123")
    password_field.send_keys(Keys.RETURN)

     # Wait for the page to load and the "Download Data" button to appear
    print("Login Execute!!")
    
    download_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Download Data"))
    )

    # Click the "Download Data" button
    download_button.click()
    print("Download EXECUTE!!!!")

    # # Wait for the download to complete (adjust the time if needed)
    # # time.sleep(10)


except Exception as e:
    print("An error occurred:", e)

finally:
    pass
    # Close the driver
    # driver.quit()

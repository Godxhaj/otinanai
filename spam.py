import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Instagram credentials from environment variables
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

if not USERNAME or not PASSWORD:
    print("Error: Missing IG_USERNAME or IG_PASSWORD environment variables.")
    sys.exit(1)

# Get the post URL from the command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 comment_instagram.py <POST_URL>")
    sys.exit(1)

POST_URL = sys.argv[1]
COMMENT_TEXT = "This is an automated comment!"

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: Run in headless mode (no GUI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Step 1: Log in to Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)
    print("Logged in successfully!")

    # Step 2: Navigate to the post
    driver.get(POST_URL)
    time.sleep(5)
    print(f"Navigated to the post: {POST_URL}")

    # Step 3: Post the comment
    comment_box = driver.find_element(By.CSS_SELECTOR, "textarea")
    comment_box.click()
    time.sleep(1)

    comment_box.send_keys(COMMENT_TEXT)
    comment_box.send_keys(Keys.RETURN)

    time.sleep(3)
    print("Comment posted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed. Script completed!")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

def read_credentials(file_path):
    with open(file_path, 'r') as file:
        username, password = [line.strip() for line in file.readlines()]
    return username, password

def login_twitter(driver, username, password):
    driver.get('https://twitter.com/login')

    try:
        username_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Phone, email, or username"]/ancestor::label//input'))
        )
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]/ancestor::div[@role="button"]'))
        )

        username_field.send_keys(username)
        next_button.click()
        time.sleep(2)

        password_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
        )
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]'))
        )

        password_field.send_keys(password)
        login_button.click()
        time.sleep(2)

    except TimeoutException:
        print("Timeout: unable to locate login elements.")

def block_user(driver, user_to_block):
    # Navigate to the user's profile page
    driver.get(f'https://twitter.com/{user_to_block}')

    try:
        # Check if the user is already blocked
        blocked_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Blocked')]"))
        )
        print(f"User {user_to_block} is already blocked.")
        return

    except TimeoutException:
        # User is not blocked, continue with blocking process
        pass

    try:
        # Click on the three-dot menu button
        menu_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='userActions']"))
        )
        menu_button.click()

        # Find the 'Block' button in the dropdown menu
        block_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem'][@data-testid='block']"))
        )
        block_button.click()

        # Confirm the block action in the modal
        confirm_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][@data-testid='confirmationSheetConfirm']"))
        )
        confirm_button.click()

        print(f"User {user_to_block} has been successfully blocked.")

    except NoSuchElementException as e:
        print(f"Unable to block user {user_to_block}: {e}")


def block_users_from_list(file_path):
    with open(file_path, 'r') as file:
        users_to_block = [line.strip() for line in file.readlines()]

    with open('browser.txt', 'r') as f:
        browser_name = f.readline().strip()

    # Initialize web driver based on browser name
    if browser_name.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name.lower() == 'edge':
        driver = webdriver.Edge()
    else:  # Default to Chrome
        driver = webdriver.Chrome()

    username, password = read_credentials('personal.txt')
    login_twitter(driver, username, password)

    for user in users_to_block:
        block_user(driver, user)

    driver.quit()

if __name__ == '__main__':
    # Replace 'user_list.txt' with the path to your txt file containing the usernames to block
    user_list_path = 'accounts.txt'
    block_users_from_list(user_list_path)
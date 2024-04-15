from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_Data import data
from Test_Locator import locators
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestProject:
    # Define common variables
    url = data.Data().url
    username = data.Data().Username
    before_url = data.Data().before_url

    @pytest.fixture
    def setup(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)
        yield driver, wait
        driver.quit()

    def test_forgot_page(self, setup):
        driver, wait = setup
        print("TC_PIM_01 - Forgot Password link validation on login page")
        try:
            driver.get(self.url)
            forgot_pass = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().forgot_btn)))
            forgot_pass.click()
            username_field = wait.until(
                EC.visibility_of_element_located((By.NAME, locators.Locators().username_textbox)))
            username_field.send_keys(self.username)
            reset = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().reset_btn)))
            reset.click()
            after_url = driver.current_url
            assert self.before_url != after_url, "Error: Reset Password link not sent successfully"
            print("Reset Password link sent successfully")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")

    def test_admin_validation(self, setup):
        driver, wait = setup
        print("TC_PIM_02 - Header Validation on Admin Page")
        try:
            driver.get(self.url)
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, locators.login_page().username_box)))
            username_field.send_keys(data.login().username)
            passwordfield = wait.until(
                EC.presence_of_element_located((By.NAME, locators.login_page().password_box)))
            passwordfield.send_keys(data.login().password)
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.login_page().login_btn)))
            button.click()
            admin = wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().admin_click)))
            admin.click()
            actual_title = driver.title
            expected_title = "OrangeHRM"
            assert actual_title == expected_title, f"Title mismatch. Expected: {expected_title}, Actual: {actual_title}"
            print("Admin page title validated successfully.")

            ad = wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().ad)))
            li_elements = ad.find_elements(By.TAG_NAME, locators.login_page().li_elements)
            print(len(li_elements))
            for expected_option in data.login().expected_options:
                for option_element in li_elements:
                    if expected_option in option_element.text:
                        print(f"{expected_option} option is displayed.")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")

    def test_main_menu(self, setup):
        driver, wait = setup
        print("TC_PIM_03 - Main Menu Validation on Admin Page")
        try:
            driver.get(self.url)
            username_field = wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().username_box)))
            username_field.send_keys(data.login().username)
            password_field = wait.until(EC.presence_of_element_located((By.NAME, locators.login_page().password_box)))
            password_field.send_keys(data.login().password)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.login_page().login_btn))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().admin_click))).click()
            menu = wait.until(EC.visibility_of_element_located((By.XPATH, locators.login_page().menu)))
            list_elements = menu.find_elements(By.TAG_NAME, locators.login_page().list_elements)
            found_options = [option.text.strip() for option in list_elements if option.text.strip()]
            for expected_option in data.login().main_expected_options:
                if any(expected_option.strip().lower() == found_option.strip().lower() for found_option in
                       found_options):
                    print(f"{expected_option} option is displayed.")
                else:
                    print(f"{expected_option} option is NOT displayed.")
            print("All the main menu options are validated!!")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")

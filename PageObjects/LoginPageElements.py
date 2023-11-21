from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPageElementsData:

    image_logo_xpath = "//img[@alt='company-branding']"
    txt_username_name = "username"
    txt_password_name = "password"
    btn_login_xpath = "//button[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
    def check_logo_is_presented(self):
        self.logo_status = self.driver.find_element(by=By.XPATH, value=self.image_logo_xpath)
        self.logo_status_flag = self.logo_status.is_displayed()
        return self.logo_status_flag

    def set_login_username(self, login_username):
        self.set_username = self.driver.find_element(by=By.NAME, value=self.txt_username_name)
        self.set_username.send_keys(login_username)

    def set_login_password(self, login_password):
        self.set_password = self.driver.find_element(by=By.NAME, value=self.txt_password_name)
        self.set_password.send_keys(login_password)

    def click_login_btn(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_login_xpath).click()



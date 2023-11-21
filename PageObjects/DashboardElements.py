from selenium import webdriver
from selenium.webdriver.common.by import By


class DashboardElementsData:

    text_dashboard_xpath = "//h6[normalize-space()='Dashboard']"
    btn_logoutdropdown_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def check_dashboard_logo_ispresented(self):
        self.dashboard_status = self.driver.find_element(by=By.XPATH, value=self.text_dashboard_xpath)
        self.dashboard_text_status = self.dashboard_status.is_displayed()
        return self.dashboard_text_status

    def click_logout_dropdown_btn(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_logoutdropdown_xpath).click()

    def click_logout_link_btn(self):
        self.driver.find_element(by=By.XPATH, value=self.link_logout_xpath).click()


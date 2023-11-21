import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.DashboardElements import DashboardElementsData
from PageObjects.LoginPageElements import LoginPageElementsData
from utilities.ReadProperties import ReadConfigData
from utilities.customlogger import LoggerGen


class TestLoginOrangeHRMTC:
    base_url = ReadConfigData.get_application_url()
    logger = LoggerGen.log_generator()

    @pytest.mark.graphicaltesting
    def test_check_logo_presented(self, browser_setup_cli):
        self.driver = browser_setup_cli
        self.logger.info("*** tc_001_test_check_logo_presented execution is started ****")
        self.driver.get(self.base_url)
        self.logger.info(" *** Orangehrm application got opened ***")
        self.driver.maximize_window()
        time.sleep(10)
        try:
            lped = LoginPageElementsData(self.driver)
            orangehrm_logo_status = lped.check_logo_is_presented()
            self.logger.info("*** Logo verification got completed")
            #time.sleep(5)
            self.driver.close()
            assert orangehrm_logo_status == True
            self.logger.info("*** tc_001_test_check_logo_presented execution is completed ***")
        except:
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_login_fun(self, browser_setup_cli):
        self.driver = browser_setup_cli
        self.logger.info("*** TC_001 login testcase execution is started")
        self.driver.get(self.base_url)
        self.logger.info("*** Orangehrm application got opened ***")
        self.driver.maximize_window()
        lped = LoginPageElementsData(self.driver)
        lped.set_login_username(ReadConfigData.get_username())
        lped.set_login_password(ReadConfigData.get_password())
        lped.click_login_btn()
        #time.sleep(7)
        dbep = DashboardElementsData(self.driver)
        try:
            self.dashboard_status = dbep.check_dashboard_logo_ispresented()
            self.logger.info("*** TC_001 dashboard text is verified")
            print(self.dashboard_status)
            self.driver.close()

            if(self.dashboard_status == True):
                assert True
                self.logger.info("*** TC_001 login testcase execution is completed")
        except:
            self.driver.save_screenshot(os.path.abspath(os.getcwd()) + "//Screenshots" + "//test_login_failure.png");
            self.driver.close()
            self.logger.info("*** TC_001 login testcase got failed")
            assert False





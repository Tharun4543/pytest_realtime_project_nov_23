import os
import time

import pytest
from selenium import webdriver

from PageObjects.DashboardElements import DashboardElementsData
from PageObjects.LoginPageElements import LoginPageElementsData
from utilities.ReadProperties import ReadConfigData
from utilities.XLutils_functions_file  import *
from utilities.customlogger import LoggerGen


class TestOrangeHRMDDT:
    base_url = ReadConfigData.get_application_url()
    logger = LoggerGen.log_generator()
    login_excel_path = ReadConfigData.get_excel_login_data_path()
    login_result_data = []

    @pytest.mark.functional
    @pytest.mark.smoke
    def test_login_orangehrm_ddt(self, browser_setup_cli):
        self.driver = browser_setup_cli
        self.logger.info("TC_002 execution got started")
        self.driver.get(self.base_url)
        self.logger.info("TC_002 orangehrm application is opened")
        self.driver.maximize_window()
        self.row_count = getRowCount(self.login_excel_path, "Sheet1")
        self.col_count = getColumnCount(self.login_excel_path, "Sheet1")
        for row in range(2, self.row_count +1):
                self.username = readData(self.login_excel_path, "Sheet1",row,1)
                self.password = readData(self.login_excel_path, "Sheet1",row,2)
                lpedlg = LoginPageElementsData(self.driver)
                lpedlg.set_login_username(self.username)
                lpedlg.set_login_password(self.password)
                lpedlg.click_login_btn()
                # time.sleep(7)
                dbeplg = DashboardElementsData(self.driver)
                try:
                    self.dashboard_status = dbeplg.check_dashboard_logo_ispresented()
                    self.logger.info("*** TC_002 dashboard text is verified")
                    if(self.dashboard_status == True):
                        dbeplg.click_logout_dropdown_btn()
                        dbeplg.click_logout_link_btn()
                        self.login_result_data.append("pass")
                        self.logger.info("*** TC_002 login testcase execution is completed")
                except:
                    self.login_result_data.append("fail")
                    self.logger.info("*** TC_002 login testcase got failed")


        if "fail" not in self.login_result_data:
            assert True
        else:
            assert False
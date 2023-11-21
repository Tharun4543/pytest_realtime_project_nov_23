import configparser
import os
config = configparser.RawConfigParser()
config.read(os.path.abspath(os.getcwd() + "//configurations//config.ini"))
class ReadConfigData:
    @staticmethod
    def get_application_url():
        application_url = config.get('Common Info', 'base_url')
        return application_url

    @staticmethod
    def get_username():
        apl_user_name = config.get('Common Info', 'user_name')
        return apl_user_name

    @staticmethod
    def get_password():
        apl_password = config.get('Common Info', 'password')
        return apl_password

    @staticmethod
    def get_excel_login_data_path():
        login_data_path = config.get('Common Info', 'login_data_excel_path')
        return login_data_path

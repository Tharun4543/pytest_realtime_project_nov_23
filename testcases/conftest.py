import os.path
from datetime import datetime

import pytest
from selenium import webdriver
'''@pytest.fixture()
def browser_setup():
    driver = webdriver.Chrome()
    return driver

'''
@pytest.fixture()
def browser_setup_cli(browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.project_name = "OrangeHRM"
    config.module_name = "test_001_LoginOrangeHrm"
    config.tester = "Tharun Nagiri"


def pytest_metadata(config):
    if 'JAVA-HOME' in config.option.metadata:
        del config.option.metadata['JAVA-HOME']

    if 'plugins' in config.option.metadata:
        del config.option.metadata['plugins']

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    #config.option.htmlpath = os.path.abspath(os.getcwd()) + "//Reports//test_summary" + datetime.strftime("%Y-%m-%d %H:%M:%S") + ".html"
    # Create a datetime object
    current_datetime = datetime.now()
    # Format the datetime object as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d%H-%M-%S")
    # Create the HTML path using the formatted datetime
    config.option.htmlpath = os.path.abspath(os.getcwd()) + "//Reports//summary_" + formatted_datetime + ".html"
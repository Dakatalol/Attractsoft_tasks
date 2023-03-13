import pytest
import os

from Utils.webdriver_utility import WebdriverManager


def pytest_addoption(parser):
    """A list of additional command line arguments"""
    parser.addoption('--browser', action='store', default='chrome', help='Select browser configuration to use')


def pytest_configure(config):
    """Sets the command line arguments to configuration options"""
    os.environ['browser'] = config.getoption('browser')


def get_base_url():
    """
    Get the initial URL for all tests

    Returns:
        str: The base URL
    """
    return f"https://www.amazon.com/"


@pytest.fixture(autouse=True)
def browser_init():
    """
    Initialize the browser every test

    Notes:
        Before Each Test:
        Navigates to the base URL

        After Each Test:
        Clears cookies and cache and resets the browser
    """
    # Run Before Each Test
    WebdriverManager.create_driver(os.environ['browser'])
    web_driver = WebdriverManager.get_driver()

    base_url = get_base_url()
    web_driver.get(base_url)
    yield

    # Run After Each Test
    web_driver.execute_script('window.sessionStorage.clear();')
    web_driver.execute_script('window.localStorage.clear();')
    web_driver.execute_script('localStorage.clear()')
    web_driver.delete_all_cookies()
    web_driver.get('about:blank')
    web_driver.quit()

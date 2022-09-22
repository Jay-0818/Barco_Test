from environment import config, browers_driver
import os
import pytest

run_webdriver = browers_driver.mapping_browser[config.BROWSER]()

@pytest.fixture(scope="class")
def driver():
    run_webdriver = browers_driver.mapping_browser[config.BROWSER]()
    yield run_webdriver
    run_webdriver.quit()



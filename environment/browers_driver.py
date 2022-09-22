from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

def chromebrowser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(" --disable-gpu ")
    chrome_options.add_argument(" --start-maximized ")
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    chrome_driver.maximize_window()
    return chrome_driver

mapping_browser = {"CHROME": chromebrowser,
                    }
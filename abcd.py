from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import os
#from Appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_cap = {
    # Set your access credentials
  "browserstack.user" : "mamidigowtham_rEU3yT",
  "browserstack.key" : "fqDEjJzF2A3usWFsoU59",
    "app" : "bs://4267b23b40ca862813f69d9051ebd72da896da99",
    "os": "Android",
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
    "project" : "First Python Local project",
  "build" : "browserstack-build-1",
  "name" : "local_test"
    #..
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

search_input1 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "com.example.exam:id/editTextTextPersonName"))
)
search_input1.send_keys("mamidi gowtham")
time.sleep(5)

search_input2 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "com.example.exam:id/editTextTextPersonName2"))
)
search_input2.send_keys("Student")
time.sleep(5)
search_input2 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "com.example.exam:id/editTextTextPersonName3"))
)
search_input2.send_keys("divya srivastav")
time.sleep(5)

search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert(len(search_results) > 0)

driver.quit()
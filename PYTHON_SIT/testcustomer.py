import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService

def test_input1():
    chrome_driver_path = "D:\webdriver\chromedriver.exe"
    service = ChromeService(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("http://127.0.0.1/Customerphp/customer.php")

    name = driver.find_element(By.ID, "firstName")
    last = driver.find_element(By.ID, "lastName")
    age = driver.find_element(By.ID, "age")
    drp_title = Select(driver.find_element(By.ID, "title"))
    drp_title.select_by_index(0)

    name.send_keys("johnjohn")
    last.send_keys("canonc")
    age.send_keys("2")

    submit = driver.find_element(By.ID, "submit")
    submit.click()

    time.sleep(1)  # Adjust the sleep time based on your application's responsiveness

    result = driver.find_element(By.ID, "firstName").text
    assert result == "First Name: johnjohn"

    driver.close()

# Call the test function
test_input1()
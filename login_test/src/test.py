from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_invalid_login():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)  

    error_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in error_message
  
    driver.save_screenshot("test-sonucu.png")

    driver.quit()

if __name__ == "__main__":
    test_invalid_login()


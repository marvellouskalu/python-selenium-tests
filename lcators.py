from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.thiscodeworks.com/extension/signup")

username = driver.find_element(By.ID, "username-login")
username.send_keys("fname")

password = driver.find_element(By.ID, "password-login")
password.send_keys("password1234")

email = driver.find_element(By.ID, "email-login")
email.send_keys("fname@gmail.com")



input("Press Enter to quit the browser...")
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("enterurl")

first_name = driver.find_element(By.CSS_SELECTOR, "#FirstName")
first_name.send_keys("fname")

last_name = driver.find_element(By.CSS_SELECTOR, "#LastName")
last_name.send_keys("lname")

email = driver.find_element(By.CSS_SELECTOR, "#EmailAddr")
email.send_keys("randomemail@gmail.com")

password = driver.find_element(By.CSS_SELECTOR, "#Passwd")
password.send_keys("pasword1234+")

checkbox = driver.find_element(By.CSS_SELECTOR, "#Tos")
checkbox.click()

submit = driver.find_element(By.CSS_SELECTOR, "#signup-button")
submit.click()

# Check for validation errors
wait = WebDriverWait(driver, 5)
error_messages = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[for='Passwd'] ul li")))

if error_messages:
    print("Form submission failed. Correcting data...")

    # Clear the form fields
    first_name.clear()
    last_name.clear()
    email.clear()
    password.clear()

    # Enter corrected data
    first_name.send_keys("new_username")
    last_name.send_keys("new_password")
    email.send_keys("new_email2w@gmail.com")
    password.send_keys("new_pasword12345+")


else:
    print("Form submitted successfully!")






input("Press Enter to quit the browser...")
driver.quit()



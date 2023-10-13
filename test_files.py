# Import necessary libraries (no changes needed here)
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Define a function to read data from the CSV file
def read_test_data_from_csv(file_path):
    test_data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_data.append(row)
    return test_data

# Path to your CSV file (change this to your CSV file's path)
csv_file_path = 'test_details.csv'


# Use pytest's parametrize decorator to run the test with different data from the CSV
@pytest.mark.parametrize("test_data", read_test_data_from_csv(csv_file_path))
def test_submit_login_form(test_data):
    # Set up the WebDriver (no changes needed here)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.thiscodeworks.com/extension/signup")

    # Fill out the form using the data from the CSV file

    # Input your own information here:
    # Update the field names to match the columns in your CSV file


    username_field = driver.find_element(By.ID, "username-login")
    username_field.send_keys(test_data['username'])  # Use the correct column name

    password_field = driver.find_element(By.ID, "password-login")
    password_field.send_keys(test_data['password'])  # Use the correct column name

    email_field = driver.find_element(By.ID, "email-login")
    email_field.send_keys(test_data['email'])  # Use the correct column name


    # Submit the form (no changes needed here)
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    # Wait for success message to appear in the title (no changes needed here)
    WebDriverWait(driver, 10).until(EC.title_contains("Success"))

    # Check for success message in title (no changes needed here)
    title = driver.title

    # Check if the expected success message is present in the title (no changes needed here)
    assert "Success" in title, "'Success' is not in the title"

    # Close the WebDriver (no changes needed here)
    driver.quit()

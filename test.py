import pytest
from selenium import webdriver

@pytest.mark.parametrize("name, email, message", [
    ("John Doe", "john.doe@example.com", "This is a test message"),
    ("Alice Smith", "alice.smith@example.com", "Another test message"),
    # Add more data sets here
])
def test_submit_contact_form(name, email, message):
    driver = webdriver.Chrome()
    driver.get("https://example.com/contact")

    # Fill out the form
    name_field = driver.find_element_by_id("name")
    email_field = driver.find_element_by_id("email")
    message_field = driver.find_element_by_id("message")

    name_field.send_keys(name)
    email_field.send_keys(email)
    message_field.send_keys(message)

    # Submit the form
    submit_button = driver.find_element_by_id("submit")
    submit_button.click()

    # Check for success message
    success_message = driver.find_element_by_id("success-message")
    assert success_message.text == "Form submitted successfully"

    driver.quit()

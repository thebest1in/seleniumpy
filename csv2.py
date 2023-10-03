import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def perform_login(email, password):
    # Set the path to the Microsoft Edge WebDriver executable
    edge_driver_path = 'C:\\edgedriver\\msedgedriver.exe'
    
    # Create Edge WebDriver instance with specified options
    options = webdriver.EdgeOptions()
    # Create a WebDriver service with the executable path
    service = webdriver.EdgeService(executable_path=edge_driver_path)
    
    # Initialize the Edge browser
    browser = webdriver.Edge(service=service, options=options)
    
    # Maximize the browser window
    browser.maximize_window()
    
    # Navigate to the LambdaTest login page
    browser.get('https://accounts.lambdatest.com/login?_gl=1*kscq4z*_gcl_au*MTA2ODc1OTI4Ny4xNjk1NzMyOTM3')
    
    try:
        # Wait for the email input field to become visible
        email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        
        # Enter the email address
        email_input.send_keys(email)
        
        # Find and click the password input field
        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        
        # Enter the password
        password_input.send_keys(password)
        
        # Find and click the login button
        login_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
        login_button.click()
        
        # Sleep for 10 seconds (you might want to use WebDriverWait for elements after login)
        time.sleep(10)
        
        # If you reach this point, the login was successful
        return True
        
    except TimeoutException:
        # Login failed
        return False
    
    finally:
        # Close the browser
        browser.quit()

# Create a CSV reader for input data
with open('Classeur1.csv', 'r') as input_file:
    csv_reader = csv.DictReader(input_file)
    
    for row in csv_reader:
        num_cas_test = row['Num_cas_test']
        email = row['mail']
        password = row['pwd']
        
        result = perform_login(email, password)
        
        # Print "OK" or "KO" based on the result
        if result:
            print(f"Test {num_cas_test}: 0")
        else:
            print(f"Test {num_cas_test}: 1")

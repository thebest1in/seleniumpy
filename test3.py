import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time  # Importez la bibliothèque time pour ajouter un délai

if __name__ == '__main__':
    # Set the path to the Microsoft Edge WebDriver executable
    edge_driver_path = 'C:\\edgedriver\\msedgedriver.exe'
    
    # Create Edge WebDriver instance with specified options
    options = webdriver.EdgeOptions()
    
    # Create a WebDriver service with the executable path
    service = webdriver.EdgeService(executable_path=edge_driver_path)
    
    # Initialize the Edge browser
    browser = webdriver.Edge(service=service, options=options)
    
    browser.maximize_window()
    browser.get('https://lambdatest.github.io/sample-todo-app/')
    
    try:
        # ... Votre code existant ...
        
        # Sleep for 5 seconds (you may want to use WebDriverWait for elements here)
        time.sleep(60)  # Ajoutez un délai de 5 secondes
        
    except TimeoutException:
        print("Element not found")
    
    # Close the browser
    browser.quit()
    
    # Ajoutez un délai d'exécution de 10 secondes à la fin du script
    time.sleep(60)  # Délai d'exécution supplémentaire de 10 secondes

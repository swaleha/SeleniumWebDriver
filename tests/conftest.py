"""  
This module contains shared fixtures
"""

import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    
    # Initialize the chrome driver instance
    b = selenium.webdriver.Chrome()
    
    # Wait for 10 seconds for the elements to appear
    b.implicitly_wait(10)
    
    # Return the WebDriver instance for setup
    yield b
    
    # Quit the WebDriver instance for cleanup
    b.quit()
    
    
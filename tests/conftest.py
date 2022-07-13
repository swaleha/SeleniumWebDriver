"""  
This module contains shared fixtures
"""
import json
import pytest
import selenium.webdriver

@pytest.fixture

def config(scope="session"):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
        
    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config
   
   
@pytest.fixture  
def browser(config):
    
    # Initialize the webdriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    # Wait for 10 seconds for the elements to appear
    b.implicitly_wait(config["implicit_wait"])
    
    # Return the WebDriver instance for setup
    yield b
    
    # Quit the WebDriver instance for cleanup
    b.quit()
    
    

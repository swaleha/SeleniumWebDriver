""" 
This module contains DuckDuckGoResult page,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By

class DuckDuckGoResult:

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result-title-a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    
    def __init__(self):
        self.browser = browser
        
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles
    
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
    
    def title(self):
        return self.browser.title
"""
These tests cover DuckDuckGo search
"""
import pytest
from pages.search import DuckDuckGoSearchPage 
from pages.result import DuckDuckGoResultPage

@pytest.mark.parametrize('phrase',['panda', 'python','polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    
    # Given the DuckDuckGo search homepage is displayed
    search_page.load()
    
    # When the user searches for "panda"
    search_page.search(phrase)
    
    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()
    
    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [title for title in titles if phrase.lower() in title.lower()]
    assert len(matches) > 0
    
    # And the search result title contains "panda"
    # Placing this assertion in the last guarantees that the page title will be ready
    assert phrase in result_page.title()
    
    # raise Exception("Incomplete Test")

"""
These tests cover DuckDuckGo search
"""

from pages.search import DuckDuckGoSearchPage 
from pages.result import DuckDuckGoResultPage

def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"
    
    # Given the DuckDuckGo search homepage is displayed
    search_page.load()
    
    # When the user searches for "panda"
    search_page.search(PHRASE)
    
    # Then the search result title contains "panda"
    assert PHRASE in result_page.title()
    
    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()
    
    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [title for title in titles if PHRASE.lower() in title.lower()]
    assert len(matches) > 0
    
    raise Exception("Incomplete Test")

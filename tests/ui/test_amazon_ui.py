import pytest
from modules.ui.page_objects.amazon_main_page import AmazonMainPage

@pytest.mark.ui
def test_search_amazon_product():
    page = AmazonMainPage()
    page.go_to()
    page.search_product("wireless mouse")
    assert "wireless mouse" in page.get_title().lower()
    page.close()
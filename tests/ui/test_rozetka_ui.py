import pytest
from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage


@pytest.mark.ui
def test_rozetka_title():
    page = RozetkaMainPage()
    page.go_to()
    assert "ROZETKA" in page.get_title().upper()
    page.close()


@pytest.mark.ui
def test_search_product_rozetka():
    page = RozetkaMainPage()
    page.go_to()
    page.search_product("смартфон Samsung")
    assert "Samsung" in page.get_page_source()
    page.close()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage


class RozetkaMainPage(BasePage):
    URL = "https://rozetka.com.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaMainPage.URL)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
    
    def search_product(self, product_name):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search_box.clear()
        search_box.send_keys(product_name)

        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-form__submit")))
        search_button.click()

    def get_title(self):
        return self.driver.title

    def get_page_source(self):
        return self.driver.page_source
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonMainPage(BasePage):
    URL = "https://www.amazon.com/"

    def __init__(self) -> None:
        super().__init__()

    #def go_to(self):
    #    self.driver.get(AmazonMainPage.URL)
    def go_to(self):
        self.driver.get(AmazonMainPage.URL)
        input("Якщо бачиш капчу — введи її в браузері, потім натисни Enter тут...")

    def search_product(self, product_name):
        wait = WebDriverWait(self.driver, 10)

        # Чекаємо, поки з’явиться поле пошуку
        search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys(product_name)

        # Чекаємо на кнопку пошуку
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
        search_button.click()

    def get_title(self):
        return self.driver.title
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Verify that {self.PAGE_URL} page is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def take_a_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    


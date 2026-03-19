from playwright.sync_api import Page
from tests.python.config import version

class Product():

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, product_id: int):
        self.page.goto(f'https://{version}.practicesoftwaretesting.com/#/product/{product_id}')
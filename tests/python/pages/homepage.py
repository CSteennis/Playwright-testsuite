from playwright.sync_api import Page
from tests.python.config import version

class Home():

    def __init__(self, page: Page):
        self.page = page
        self.product_name = page.get_by_test_id('product-name')
        self.product_price = page.get_by_test_id('product-price')

    def navigate(self):
        self.page.goto(f'https://{version}.practicesoftwaretesting.com/#/')

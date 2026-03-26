from playwright.sync_api import Page
from config import version

class Home():

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(f'https://{version}.practicesoftwaretesting.com/#/')


class Contact():

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(f'https://{version}.practicesoftwaretesting.com/#/contact')

class Product():

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, product_id: int):
        self.page.goto(f'https://{version}.practicesoftwaretesting.com/#/product/{product_id}')

class Rentals():

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(f'https://{version}.practicesoftwaretesting.com/#/rentals')

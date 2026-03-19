from playwright.sync_api import Page
from tests.python.config import version

class Contact():

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(f'https://{version}.practicesoftwaretesting.com/#/contact')

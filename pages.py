from playwright.sync_api import Page
from conf import version

class Home():

    def __init__(self, page: Page):
        self.version = version
        self.page = page

    def navigate(self):
        self.page.goto(f'https://{self.version}.practicesoftwaretesting.com/#/')

class Contact():

    def __init__(self, page: Page):
        self.version = version
        self.page = page

    def navigate(self):
        self.page.goto(f'https://{self.version}.practicesoftwaretesting.com/#/contact')
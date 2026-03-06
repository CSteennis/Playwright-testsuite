from playwright.sync_api import Page

class HomeLocators():
    def __init__(self, page: Page):
        self.product_name = page.locator('[data-test="product-name"]')
        self.product_price = page.locator('[data-test="product-price"]')



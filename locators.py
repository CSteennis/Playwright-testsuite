from playwright.sync_api import Page

class HomeLocators():
    def __init__(self, page: Page):
        self.product_name = page.get_by_test_id("product-name")
        self.product_price = page.get_by_test_id("product-price")



from playwright.sync_api import Page, expect
import pytest
import re
from locators import HomeLocators


#AC1
def test_product_overview_displayed(page: Page, homepage):
    expect(page.get_by_test_id("")).to_be_visible()

#AC2
def test_product_card_information(page: Page, homepage):
    grid = page.get_by_test_id("")
    expect(grid).to_be_visible()
    product_cards = grid.locator('.card').all()
    for pc in product_cards:
        expect(pc.get_by_role('img')).to_be_visible()
        expect(pc.get_by_test_id("product-name")).to_be_visible()
        expect(pc.get_by_test_id("product-price")).to_be_visible()

#AC3
def test_nav_product_detail(page: Page, homepage):
    n = 1 #product number
    test_product = page.get_by_test_id("product-name").first
    product_name = test_product.inner_text()
    test_product.first.click()
    expect(page).to_have_url(re.compile(rf"/product/{n}"))
    expect(page.get_by_text(product_name)).to_be_visible()



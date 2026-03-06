from playwright.sync_api import Page, expect
import pytest
import re
from locators import HomeLocators
from pages import Home

@pytest.fixture
def before_each_test(page: Page):
    Home(page).navigate()

#AC1
def test_product_overview(page: Page, before_each_test: None):
    expect(page.get_by_role('list').filter(has=page.locator('[data-test="product-1"]'))).to_be_visible()

#AC2
def test_product_card_information(page: Page, before_each_test: None):
    grid = page.get_by_role('list').filter(has=page.locator('[data-test="product-1"]'))
    expect(grid).to_be_visible()
    product_cards = grid.get_by_role('listitem').all()
    for pc in product_cards:
        loc = HomeLocators(pc)
        expect(pc.get_by_role('img')).to_be_visible()
        expect(pc.locator('[data-test="product-name"]')).to_be_visible()
        expect(pc.locator('[data-test="product-price"]')).to_be_visible()

#AC3
def test_nav_product_detail(page: Page, before_each_test: None):
    n = 1 #product number
    test_product = page.locator(f'[data-test="product-name"]').first
    product_name = test_product.inner_text()
    test_product.first.click()
    expect(page).to_have_url(re.compile(rf"/product/{n}"))
    expect(page.get_by_text(product_name)).to_be_visible()

from playwright.sync_api import Page, expect
import pytest
import re
from tests.python.pages.homepage import Home

@pytest.fixture
def home_page(page: Page, set_testid):
    Home(page).navigate()
    return page

#AC1
def test_product_overview(home_page: Page):
    expect(home_page.get_by_role('list').filter(has=home_page.get_by_test_id('product-1'))).to_be_visible()

#AC2
def test_product_card_information(home_page: Page):
    grid = home_page.get_by_role('list').filter(has=home_page.get_by_test_id('product-1'))
    expect(grid).to_be_visible()
    product_cards = grid.get_by_role('listitem').all()
    for pc in product_cards:
        expect(pc.get_by_role('img')).to_be_visible()
        expect(pc.get_by_test_id('product-name')).to_be_visible()
        expect(pc.get_by_test_id('product-price')).to_be_visible()

#AC3
def test_nav_product_detail(home_page: Page):
    n = 1 #product number
    test_product = home_page.get_by_test_id('product-name').first
    product_name = test_product.inner_text()
    test_product.first.click()
    expect(home_page).to_have_url(re.compile(rf"/product/{n}"))
    expect(home_page.get_by_text(product_name)).to_be_visible()

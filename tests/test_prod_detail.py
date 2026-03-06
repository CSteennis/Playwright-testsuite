from playwright.sync_api import Page, expect
import pytest, re

from conf import version
from pages import Home

pages = ['overview', 'category']
#AC1
@pytest.mark.parametrize('start_page', pages)
def test_prod_detail_page_displayed(page: Page, start_page):
    # Given I click on a product from the overview or category page
    Home(page).navigate()
    if start_page == 'category':
        page.locator('[data-test="nav-hand-tools"]').click()

    page.locator('[data-test="product-1"]').click()

    # Then the product detail page is displayed
    expect(page).to_have_url(re.compile(r'product/1'))

def test_prod_info_shown():
    pass
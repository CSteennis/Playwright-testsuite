from playwright.sync_api import Page, expect
import pytest, re

from pages import Home, Product

import time

pages = ['overview', 'category']
#AC1
@pytest.mark.parametrize('start_page', pages)
def test_prod_detail_page_displayed(page: Page, start_page, homepage):
    # Given I click on a product from the overview or category page
    if start_page == 'category':
        page.get_by_role('navigation').get_by_role('button', name='Categories').click()
        page.get_by_test_id('nav-hand-tools').click()

    prod_card = page.locator('.card').first
    partial_url = prod_card.get_attribute('data-test').replace('-', '/')
    prod_card.click()

    # Then the product detail page is displayed
    expect(page).to_have_url(re.compile(partial_url))

def test_prod_info_shown(page: Page, set_testid):
    # Given the product detail page is displayed
    Product(page).navigate(1)

    # Then the following information is shown:
    expect(page.get_by_role("img", name="A generic square placeholder")).to_be_visible()
    expect(page.get_by_test_id('product-name')).to_be_visible()
    expect(page.get_by_test_id('product-description')).to_be_visible()
    expect(page.get_by_test_id('unit-price')).to_be_visible()
    expect(page.get_by_label('category')).to_be_visible()
    expect(page.get_by_label('brand')).to_be_visible()

def test_related_products(page: Page):
    product_id = 1
    product_page = Product(page)
    product_page.navigate(product_id)

    expect(page.locator('div').filter(has=page.locator('.card')).last).to_be_visible()

    related_prods = page.locator('.card').all()
    for rel in related_prods:
        partial_url = rel.get_attribute('href')
        rel.click()
        expect(page).to_have_url(re.compile(partial_url))
        product_page.navigate(product_id)

from playwright.sync_api import Page, expect, Playwright
import pytest


def test_add_to_cart(product_page: Page):
    prod_name = product_page.get_by_test_id('product-name').first.inner_text()
    quantity = product_page.get_by_test_id('quantity').input_value()

    product_page.get_by_role('button', name='Add to Cart').click()
    
    expect(product_page.get_by_role('alert').filter(has_text="Product added to shopping cart.")).to_be_visible()

    # assuming shopping cart was empty
    expect(product_page.get_by_test_id('cart-quantity')).to_have_text(quantity)
    
    product_page.get_by_label('cart').click()

    expect(product_page.get_by_text(prod_name)).to_be_visible()

def test_out_of_stock(product_page: Page, playwright: Playwright):
    api = playwright.request.new_context(base_url='https://api-v3.practicesoftwaretesting.com')

    response = api.get('/products/6/')

    assert response.json()['is_rental'] == False

    # given out of stock + not rental

    expect(product_page.get_by_role('button', name='Add to Cart')).to_be_disabled()


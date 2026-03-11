from playwright.sync_api import Page, expect
import pytest

from pages import Product

@pytest.fixture
def product_page(page: Page, set_testid):
    Product(page).navigate(1)

    return page

def test_quantity_selector_displayed(product_page: Page):
    expect(product_page.get_by_test_id('decrease-quantity')).to_be_visible()
    expect(product_page.get_by_test_id('increase-quantity')).to_be_visible()
    expect(product_page.get_by_test_id('quantity')).to_be_visible()

def test_default_quantity(product_page: Page):
    expect(product_page.get_by_test_id('quantity')).to_have_value('1')

def test_increase_quantity(product_page: Page):
    start_value = product_page.get_by_test_id('quantity').input_value()
    product_page.get_by_test_id('increase-quantity').click()

    expected_value = str(int(start_value) + 1)
    expect(product_page.get_by_test_id('quantity')).to_have_value(expected_value)

def test_decrease_quantity(product_page: Page):
    product_page.get_by_test_id('quantity').fill('3')
    start_value = product_page.get_by_test_id('quantity').input_value()
    product_page.get_by_test_id('decrease-quantity').click()

    expected_value = str(int(start_value) - 1)
    expect(product_page.get_by_test_id('quantity')).to_have_value(expected_value)

def test_minimum_quantity(product_page: Page):
    expect(product_page.get_by_test_id('quantity')).to_have_value('1')
    product_page.get_by_test_id('decrease-quantity').click()

    expect(product_page.get_by_test_id('quantity')).to_have_value('1')

def test_manual_quantity_entry_valid(product_page: Page):
    product_page.get_by_test_id('quantity').fill('5')
    expect(product_page.get_by_test_id('quantity')).to_have_value('5')

def test_manual_quantity_entry_invalid_low(product_page: Page):
    product_page.get_by_test_id('quantity').fill('0')
    expect(product_page.get_by_test_id('quantity')).to_have_value('1')

def test_manual_quantity_entry_invalid_upper(product_page: Page):
    product_page.get_by_test_id('quantity').fill('1000000000')
    expect(product_page.get_by_test_id('quantity')).to_have_value('999999999')

def test_add_to_cart(product_page: Page):
    prod_name = product_page.get_by_test_id('product-name').first.inner_text()
    quantity = product_page.get_by_test_id('quantity').input_value()

    product_page.get_by_role('button', name='Add to Cart').click()
    
    expect(product_page.get_by_role('alert').filter(has_text="Product added to shopping cart.")).to_be_visible()

    # assuming shopping cart was empty
    expect(product_page.get_by_test_id('cart-quantity')).to_have_text(quantity)
    
    product_page.get_by_label('cart').click()

    expect(product_page.get_by_text(prod_name)).to_be_visible()

from playwright.sync_api import Page, expect


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

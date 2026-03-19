from playwright.sync_api import Page, expect
import pytest, re

from pages import Rentals

@pytest.fixture
def rental_page(page: Page, set_testid):
    Rentals(page).navigate()

    return page

@pytest.mark.record
def test_rental_accessible(rental_page: Page):
    expect(rental_page.get_by_test_id('page-title')).to_have_text('Rentals')
    for rental in rental_page.get_by_test_id(re.compile('product-*')).all():
        expect(rental).to_be_visible()

def test_rental_product_display(rental_page: Page):
    all_rentals = rental_page.get_by_test_id(re.compile('product-[0-9]*'))

    expect(all_rentals.first).to_be_visible()

    for rental in all_rentals.all():
        expect(rental.get_by_role('img')).to_be_visible()
        expect(rental.locator('.card-title')).to_be_visible()
        expect(rental.locator('.card-text')).to_be_visible()

def test_rental_detail_page(rental_page: Page):
    rental_page.get_by_test_id(re.compile('product-[0-9]*')).first.click()

    slider = rental_page.get_by_role('slider')
    expect(slider).to_be_visible()
    
    slider_val = slider.evaluate('(element) => {return element.getAttribute("aria-valuenow");}')    
    slider_max = slider.evaluate('(element) => {return element.getAttribute("aria-valuemax");}')

    unit_price = rental_page.get_by_test_id('unit-price').inner_text()
    total_price = rental_page.locator('#total-price')
    slider.click()

    while int(slider_val) < int(slider_max):
        slider_val = slider.evaluate('(element) => {return element.getAttribute("aria-valuenow");}')
        expected_total_price = float(unit_price) * float(slider_val)

        expect(total_price).to_have_text(f"{expected_total_price:.2f}")

        slider.press('ArrowRight')

def test_rental_label_in_checkout(rental_page: Page):
    rental_page.get_by_test_id(re.compile('product-[0-9]*')).first.click()
    product_name = rental_page.get_by_test_id('product-name').inner_text()
    rental_page.get_by_role('button', name="Add to cart").click()
    rental_page.get_by_label('cart').click()

    expect(rental_page.locator('tr').filter(has_text=product_name)).to_contain_text('This is a rental item')

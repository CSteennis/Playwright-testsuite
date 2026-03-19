import pytest

from pages import Product

@pytest.fixture
def product_page(page, set_testid):
    Product(page).navigate(1)

    return page

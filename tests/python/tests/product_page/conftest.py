import pytest

from tests.python.pages.pages import Product

@pytest.fixture
def product_page(page, set_testid):
    Product(page).navigate(1)

    return page

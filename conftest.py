import pytest
from playwright.sync_api import Playwright

version = 'v3'

@pytest.fixture(scope='session')
def set_testid(playwright: Playwright):
    playwright.selectors.set_test_id_attribute('data-test')

@pytest.fixture
def homepage(page, set_testid):
    page.goto(f'https://{version}.practicesoftwaretesting.com/#/')
    return page
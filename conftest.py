import pytest
from playwright.sync_api import Playwright

version = 'v1'

@pytest.fixture
def set_testid(playwright: Playwright):
    playwright.selectors.set_test_id_attribute('data-test')
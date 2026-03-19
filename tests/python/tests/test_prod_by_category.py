from playwright.sync_api import Locator, Page, expect
import pytest
import re
from tests.python.pages.homepage import Home
from tests.python.utils.api import APIBase

category_name_list = ['Hand Tools', 'Power Tools']

@pytest.mark.parametrize('category_name', category_name_list)
def test_category_page(page: Page, category_name, set_testid):
    homepage = Home(page)
    homepage.navigate()

    # Given I click on a category name
    page.get_by_role('link', name=category_name).click()

    # Then a page with products belonging to that category is displayed.
    cat_string = f'/category/{category_name.casefold().replace(' ', '-')}'
    expect(page).to_have_url(re.compile(cat_string))

    expect(page.get_by_test_id('page-title')).to_have_text(re.compile(category_name))


from playwright.sync_api import Page, expect
import pytest, re

def test_input_displayed(homepage: Page):
    expect(homepage.get_by_test_id('search-query')).to_be_visible()

@pytest.mark.parametrize('query', ['', 'ab'])
def test_minimum_search_len(homepage: Page, query):
    searchbox = homepage.get_by_test_id('search-query')
    searchbox.fill(query)
    homepage.get_by_role('button', name="Search").click()
    expect(homepage.get_by_role('alert', name='validation-error')).to_be_visible()

@pytest.mark.parametrize('query', ['abcdefghijklmnopqrstuvwxyz78901234567890', 'abcdefghijklmnopqrstuvwxyz7890123456789', 'abcdefghijklmnopqrstuvwxyz789012345678901'])
def test_maximum_search_len(homepage: Page, query):
    searchbox = homepage.get_by_test_id('search-query')
    searchbox.fill(query)
    homepage.get_by_role('button', name="Search").click()
    x = len(query)

    if len(query) > 40:
        expect(homepage.get_by_role('alert', name='validation-error')).to_be_visible()
    else:
        expect(homepage.get_by_role('alert', name='validation-error')).not_to_be_visible()

@pytest.mark.parametrize('query', ['hammer', 'pliers', 'thor'])
def test_results_displayed(homepage: Page,query):
    searchbox = homepage.get_by_test_id('search-query')
    searchbox.fill(query)
    homepage.get_by_role('button', name="Search").click()

    results = homepage.locator('.card').filter(has=homepage.get_by_test_id('product-name')).all()

    for result in results:
        if result.is_visible():
            expect(result.get_by_test_id('product-name')).to_have_text(re.compile(query, re.IGNORECASE))


def test_search_resets_filters(homepage: Page):
    homepage.get_by_test_id('sort').select_option('name,asc')
    homepage.get_by_test_id("category-4").check()
    homepage.get_by_test_id("category-10").check()
    homepage.get_by_test_id("category-5").check()
    homepage.get_by_test_id("brand-1").check()

    homepage.get_by_test_id('search-query').fill('query')
    homepage.get_by_test_id('search-query').click()
    
    expect(homepage.get_by_test_id('sort')).to_have_value('')
    expect(homepage.get_by_test_id("category-4")).not_to_be_checked()
    expect(homepage.get_by_test_id("category-10")).not_to_be_checked()
    expect(homepage.get_by_test_id("category-5")).not_to_be_checked()
    expect(homepage.get_by_test_id("brand-1")).not_to_be_checked()



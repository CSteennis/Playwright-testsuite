from playwright.sync_api import Page, expect
import pytest

def test_controls_displayed(page: Page, homepage):
    expect(page.get_by_label('Pagination')).to_be_visible()

def test_navigation(page: Page, homepage):
    # Click on another page using navigation
    next_page = page.get_by_role('navigation', name='Pagination')
    listitem = next_page.get_by_role('listitem').filter(has_text='3')
    listitem.click()

    # Is highlighted
    expect(listitem).to_have_class('current')

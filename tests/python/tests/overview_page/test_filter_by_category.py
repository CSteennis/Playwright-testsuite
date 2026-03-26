from playwright.sync_api import Page, expect

def test_category_filter_displayed(homepage: Page):
    for cat in homepage.get_by_role('checkbox', name='category_id').all():
        expect(cat).to_be_visible()
from playwright.sync_api import Page, expect

def test_dropdown_displayed(homepage: Page):
    expect(homepage.locator('select[data-test="sort"]')).to_be_visible()

def test_options(homepage: Page):
    expect(homepage.get_by_role('option', name='Name (A - Z)')).to_be_enabled()
    expect(homepage.get_by_role('option', name='Name (Z - A)')).to_be_enabled()
    expect(homepage.get_by_role('option', name='Price (High - Low)')).to_be_enabled()
    expect(homepage.get_by_role('option', name='Price (Low - High)')).to_be_enabled()

def test_sort_a_to_z(homepage: Page):
    homepage.get_by_test_id('sort').select_option('Name (A - Z)')
    all_titles = homepage.get_by_test_id('product-name').all_text_contents()

    assert all_titles == sorted(all_titles)

def test_sort_z_to_a(homepage: Page):
    homepage.get_by_test_id('sort').select_option('Name (Z - A)')
    all_titles = homepage.get_by_test_id('product-name').all_text_contents()

    assert all_titles == sorted(all_titles, reverse=True)

def test_sort_high_to_low(homepage: Page):
    homepage.get_by_test_id('sort').select_option('Price (High - Low)')
    all_titles = [float(x.strip('$')) for x in homepage.get_by_test_id('product-price').all_text_contents()]

    assert all_titles == sorted(all_titles)

def test_sort_low_to_high(homepage: Page):
    homepage.get_by_test_id('sort').select_option('Price (Low - High)')
    all_titles = [float(x.strip('$')) for x in homepage.get_by_test_id('product-price').all_text_contents()]

    assert all_titles == sorted(all_titles, reverse=True)

    

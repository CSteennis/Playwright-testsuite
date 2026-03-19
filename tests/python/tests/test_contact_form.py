from playwright.sync_api import Locator, Page, expect
import pytest

from tests.python.pages.contactpage import Contact

dummy_data = {
    'first_name': 'Foo',
    'last_name': 'Bar',
    'email': 'foo@bar.com',
    'subject': 'Webmaster',
    'msg': 'this msg is a fifty character long message exactly'
}

dummy_data1 = {
    'first_name': 'Foo',
    'last_name': 'Bar',
    'email': 'foo@bar.com',
    'subject': 'Return',
    'msg': 'this is a fifty character long message containing exactly enough information to be fifty characters long.'
}

@pytest.fixture
def contact_form(page: Page, set_testid):
    # Given I navigate to the contact page
    Contact(page).navigate()
    
    # Then a contact form is displayed
    form = page.locator('form')
    expect(form).to_be_visible()

    return form

def test_fields(contact_form: Locator):
    expect(contact_form.get_by_label('First name')).to_be_visible()
    expect(contact_form.get_by_label('Last name')).to_be_visible()
    expect(contact_form.get_by_label('Subject')).to_be_visible()
    expect(contact_form.get_by_label('Email')).to_be_visible()
    expect(contact_form.get_by_label('Email')).to_have_attribute('type', 'email')
    expect(contact_form.get_by_label('Message')).to_be_visible()

def test_subject_options(contact_form: Locator):
    # Given dropdown is displayed
    dropdown = contact_form.get_by_label('Subject')
    expect(dropdown).to_be_visible()

    # Then it has the following options
    options = [
        "Select a subject", # needed to handle placeholder
        "Customer service",
        "Webmaster",
        "Return",
        "Payments",
        "Warranty",
        "Status of my order",
    ]

    real_options = dropdown.locator('option')

    expect(real_options).to_have_count(len(options))

    for expected_option, real_option in zip(options, real_options.all()):
        expect(real_option).to_have_text(expected_option)

@pytest.mark.parametrize('message', ["", "less than 50"])
def test_message_minimum_len(page: Page, contact_form: Locator, message):
    # Given I enter a message with fewer than 50 chars
    contact_form.get_by_label('Message').fill(message)
    contact_form.get_by_role('button', name='Send').click()
    
    # Then a validation error is shown indicating the message must be at least 50 characters
    expect(page.get_by_test_id('message-error')).to_be_visible()
    if len(message) > 0:
        expect(page.get_by_test_id('message-error').get_by_text('50 characters')).to_be_visible()

@pytest.mark.parametrize('message', [dummy_data['msg'], dummy_data1['msg']])
def test_message_len(page: Page, contact_form: Locator, message):
    # Given I enter a message with fewer than 50 chars
    contact_form.get_by_label('Message').fill(message)
    contact_form.get_by_role('button', name='Send').click()
    
    # Then a validation error is shown indicating the message must be at least 50 characters
    expect(page.get_by_test_id('message-error')).not_to_be_visible()
    
def test_succesfull_submission(page: Page, contact_form: Locator):
    # Given all required fields are filled in
    contact_form.get_by_label('First name').fill(dummy_data['first_name'])
    contact_form.get_by_label('Last name').fill(dummy_data['last_name'])
    contact_form.get_by_label('Email').fill(dummy_data['email'])
    contact_form.get_by_label('Subject').select_option(dummy_data['subject'])
    contact_form.get_by_label('Message').fill(dummy_data1['msg'])

    # When I submit the contact form
    contact_form.get_by_role('button', name='Send').click()

    # Then a confirmation message is displayed
    expect(page.get_by_text('Thanks for your message! We will contact you shortly.')).to_be_visible()

    # And the form is hidden
    expect(contact_form).to_be_hidden()


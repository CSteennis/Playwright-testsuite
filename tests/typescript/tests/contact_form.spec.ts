import { expect, type Page } from '@playwright/test'
import { test } from '../fixtures/contact-page.fixture'
import { subjectOptions, messageCases, formData, formSuccessText } from '../data_generators/contact-page-data'

test.describe("Test contact form", () => {
    test("test form visibility", async ({ contactPage }) => {
        // Given I navigate to the contact page
        // Then a contact form is displayed
        await expect(contactPage.contactForm).toBeVisible()
    });

    test('test field visability', async ({ contactPage }) => {
        await expect(contactPage.firstName).toBeEnabled()
        await expect(contactPage.lastName).toBeVisible()
        await expect(contactPage.subject).toBeVisible()
        await expect(contactPage.email).toBeVisible()
        await expect(contactPage.email).toHaveAttribute('type', 'email')
        await expect(contactPage.message).toBeVisible()
    });

    test('test subject dropdown', async ({ contactPage }) => {
        // Given dropdown is displayed
        const dropdownOptions = contactPage.getSubjectOptions()
        // Then it has the correct options
        await expect(dropdownOptions).toHaveText(subjectOptions)
    });

    messageCases.forEach(({ name, message, expectedError }) => {
        test(`test message length - ${name}`, async ({ contactPage }) => {
            await contactPage.fillMessageField(message)
            await contactPage.submitForm()
            if (expectedError != '') {
                await expect(contactPage.getMessageAlert()).toBeVisible()
                await expect(contactPage.getMessageAlert()).toHaveText(expectedError)
            } else {
                await expect(contactPage.getMessageAlert()).toBeHidden()
            }
        });
    });

    test('test succesfull submission', async ({ contactPage }) => {
        // Given all required fields are filled in
        await contactPage.fillForm(formData)
        // When I submit the contact form
        await contactPage.submitForm()
        // Then a confirmation message is displayed
        await expect(contactPage.getFormSubmittedAlert()).toBeVisible()
        await expect(contactPage.getFormSubmittedAlert()).toHaveText(formSuccessText)
        // And the form is hidden
        await expect(contactPage.contactForm).toBeHidden()
    });
});

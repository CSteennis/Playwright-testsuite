import { expect, type Page } from '@playwright/test'
import { test } from '../fixtures/contact-page.fixture'
import { subjectOptions, messageCases, formData, formSuccessText } from '../data_generators/contact-page-data'

test.describe("Test contact form", () => {
    test("test form visibility", async ({ contactPage }) => {
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
        const dropdownOptions = contactPage.getSubjectOptions()
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
        await contactPage.fillForm(formData)
        await contactPage.submitForm()
        await expect(contactPage.getFormSubmittedAlert()).toBeVisible()
        await expect(contactPage.getFormSubmittedAlert()).toHaveText(formSuccessText)
    });
});

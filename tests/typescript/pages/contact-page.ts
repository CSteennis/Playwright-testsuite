import type { Locator, Page } from '@playwright/test'
import { baseURL } from '../config'

export type ContactFormData = {
    firstName: string
    lastName: string
    subject: string
    email: string
    message: string
}

export class ContactPage {
    readonly page: Page
    readonly contactForm: Locator
    readonly firstName: Locator
    readonly lastName: Locator
    readonly subject: Locator
    readonly email: Locator
    readonly message: Locator
    readonly submit: Locator

    constructor(page: Page) {
        this.page = page
        this.contactForm = page.locator('form')
        this.firstName = page.getByLabel('First name')
        this.lastName = page.getByLabel('Last name')
        this.subject = page.getByLabel('Subject')
        this.email = page.getByLabel('Email')
        this.message = page.getByLabel('Message')
        this.submit = page.getByRole('button', { name: 'Send' })
    }

    async goto(): Promise<void> {
        await this.page.goto(`${baseURL}/contact`)
    }

    getMessageAlert(): Locator {
        return this.page.getByRole('alert').filter({ hasText: 'Message' })
    }

    getFormSubmittedAlert(): Locator {
        return this.page.getByRole('alert').and(this.page.locator('.alert-success'))
    }

    getSubjectOptions(): Locator {
        return this.subject.locator('option')
    }

    async fillForm(form: ContactFormData): Promise<void> {
        await this.firstName.fill(form.firstName)
        await this.lastName.fill(form.lastName)
        await this.subject.selectOption({ label: form.subject })
        await this.email.fill(form.email)
        await this.message.fill(form.message)
    }

    async fillMessageField(message: string): Promise<void> {
        await this.message.fill(message)
    }

    async submitForm(): Promise<void> {
        await this.submit.click()
    }
}


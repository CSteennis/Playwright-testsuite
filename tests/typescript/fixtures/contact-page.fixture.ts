import { test as base, type Locator } from '@playwright/test'
import { ContactPage } from '../pages/contact-page'

type Fixtures = {
    contactPage: ContactPage,
};

export const test = base.extend<Fixtures>({
    contactPage: async ({ page }, use) => {
        const contactPage = new ContactPage(page)
        await contactPage.goto()
        await use(contactPage)
    }
});

// export expect from '@playwright/test'
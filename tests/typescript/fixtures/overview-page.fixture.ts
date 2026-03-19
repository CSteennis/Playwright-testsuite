import { test as base, type Locator } from '@playwright/test'
import { OverviewPage } from '../pages/overview-page'

type Fixtures = {
    overviewPage: OverviewPage,
};

export const test = base.extend<Fixtures>({
    overviewPage: async ({ page }, use) => {
        const overviewPage = new OverviewPage(page)
        await overviewPage.goto()
        await use(overviewPage)
    }
});

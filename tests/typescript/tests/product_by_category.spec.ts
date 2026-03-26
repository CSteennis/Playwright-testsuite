import { expect, type Page } from '@playwright/test'
import { test } from '../fixtures/overview-page.fixture'
import { categoryNames } from '../data_generators/overview-page-data'

test.describe("test category pages", () => {
    categoryNames.forEach((categoryName) => {
        test(`test ${categoryName} page reachable`, async ({ overviewPage }) => {
            await overviewPage.gotoCategoryPage(categoryName)

            // await expect(overviewPage.page).toHaveURL()
        });
    });
});
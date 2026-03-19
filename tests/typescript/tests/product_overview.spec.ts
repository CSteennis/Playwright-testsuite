import { expect } from "@playwright/test";
import { test } from "../fixtures/overview-page.fixture";

test.describe("test product overview", () => {
    test("", async ({ overviewPage }) => {
        expect(overviewPage.page.getByRole('list').filter({ has: overviewPage.page.getByTestId('product-1') })).toBeVisible()
    });
});
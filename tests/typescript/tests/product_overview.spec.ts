import { expect } from "@playwright/test";
import { test } from "../fixtures/overview-page.fixture";
import { ProductPage } from "../pages/product-page";

test.describe("test product overview", () => {
    test("test products visible", async ({ overviewPage }) => {
        await expect(overviewPage.productList).toBeVisible()
    });

    test("test card information visible", async ({ overviewPage }) => {
        await expect(overviewPage.productList).toBeVisible()
        const productCards = await overviewPage.productCards.all()

        for (let productCard of productCards) {
            const productCardDetails = overviewPage.productDetails(productCard)
            await expect(productCardDetails.img).toBeVisible()
            await expect(productCardDetails.productName).toBeVisible()
            await expect(productCardDetails.productPrice).toBeVisible()
        }
    });

    test("test navigate to product detail page", async ({ overviewPage }) => {
        await overviewPage.clickOnFirstProduct()
        const productPage = new ProductPage(overviewPage.page)
        await expect(productPage.page).toHaveURL(/product\/1/)
        await expect(productPage.productName).toBeVisible()
    });
});
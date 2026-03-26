import type { Locator, Page } from "@playwright/test";
import { baseURL } from "../config";

type ProductCard = {
    img: Locator,
    productName: Locator,
    productPrice: Locator
}

export class OverviewPage {
    readonly page: Page
    readonly productList: Locator
    readonly productCards: Locator

    constructor(page: Page) {
        this.page = page
        this.productList = page.getByRole('list').filter({ has: page.getByTestId('product-1') })
        this.productCards = this.productList.getByRole('listitem')
        
    }

    async goto() {
        await this.page.goto(`${baseURL}/`)
    }

    productDetails(productCard: Locator): ProductCard {
        return {
            img: productCard.getByRole('img'),
            productName: productCard.getByTestId('product-name'),
            productPrice: productCard.getByTestId('product-price')
        }
    }

    async clickOnFirstProduct() {
        const testProductCard = this.productCards.first()
        const testProductDetails = this.productDetails(testProductCard)
        await testProductDetails.productName.click()
    }
}
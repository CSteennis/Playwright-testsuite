import type { Locator, Page } from "@playwright/test";
import { baseURL } from "../config";

export class ProductPage {
    readonly page: Page
    readonly productName: Locator

    constructor(page: Page) {
        this.page = page
        this.productName = page.getByRole('heading').and(page.getByTestId('product-name'))
    }

}
import type { Locator, Page } from "@playwright/test";
import { baseURL } from "../config";

export class OverviewPage {
    readonly page: Page
    readonly searchInput: Locator

    constructor(page: Page) {
        this.page = page
        this.searchInput = page.locator('input[data-test=search-query]')
    }

    async goto() {
        await this.page.goto(`${baseURL}/`)
    }
}
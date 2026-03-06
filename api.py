from playwright.sync_api import Playwright
from sprint1.conf import version

class APIBase():
    def get_cat_names(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=f'https://api-{version}.practicesoftwaretesting.com')
        response = api_request_context.get('/categories')

        assert response.ok
        print(response.json())

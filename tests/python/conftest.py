import pytest
from playwright.sync_api import Playwright, Browser

import os

version = 'v2'


@pytest.fixture()
def context(browser: Browser, request):
    results_dir = "test_result"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    node_name = request.node.name
    context = browser.new_context(record_video_dir=f"{results_dir}/tmp_videos")

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    page = context.pages[0]
    video_path = page.video.path()

    failed = request.node.rep_call.failed

    if failed:
        os.makedirs(f"{results_dir}/{node_name}", exist_ok=True)

        page.screenshot(path=f"{results_dir}/{node_name}/screenshot.png")
        
        context.tracing.stop(path=f"{results_dir}/{node_name}/trace.zip")
        context.close()

        os.replace(video_path, f"{results_dir}/{node_name}/video.webm")

        print(f"Test failed. Video saved at: {video_path}")
    else:
        context.close()
        os.remove(video_path)

@pytest.fixture(scope='session')
def set_testid(playwright: Playwright, browser):
    playwright.selectors.set_test_id_attribute('data-test')

@pytest.fixture
def homepage(page, set_testid):
    page.goto(f'https://{version}.practicesoftwaretesting.com/#/')
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
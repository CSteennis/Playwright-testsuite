import pytest
from playwright.sync_api import Playwright, Browser

import os

from config import version

@pytest.fixture()
def context(browser: Browser, request):
    results_dir = "test_result"
    os.makedirs(results_dir, exist_ok=True)

    node_name = request.node.name
    context = browser.new_context(record_video_dir=f"{results_dir}/tmp_videos")

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    yield context

    page = context.pages[0]
    video_path = page.video.path()

    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    wants_record = request.node.get_closest_marker("record") is not None

    if failed or wants_record:
        os.makedirs(f"{results_dir}/{node_name}", exist_ok=True)

        page.screenshot(path=f"{results_dir}/{node_name}/screenshot.png")
        
        context.tracing.stop(path=f"{results_dir}/{node_name}/trace.zip")
        context.close()

        os.replace(video_path, f"{results_dir}/{node_name}/video.webm")

        reason = "failed" if failed else "marked"
        print(f"Test {reason} – video saved at: {results_dir}/{node_name}/video.webm")
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
import re
from playwright.sync_api import Page, Playwright, expect


def test_playwright(page: Page):
    page.goto('https://playwright.dev/python/')

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile('Playwright'))

    # create a locator
    get_started = page.get_by_role('link', name='Get started')

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute('href', '/python/docs/intro')

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile('.*intro'))


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://vsmonitor.com/')
    page.get_by_role('link', name='angle-right icon Sign up').click()
    page.locator('#eula_button').click()
    page.get_by_role('button', name='Accept').click()
    page.locator('#tos_button').click()
    page.get_by_role('button', name='Accept').click()
    page.locator('#data-privacy_button').click()
    page.get_by_role('button', name='Accept').click()
    page.get_by_role('button').filter(has_text='close').click()
    context.close()
    browser.close()

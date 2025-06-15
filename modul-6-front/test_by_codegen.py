from playwright.sync_api import sync_playwright, Page, expect


def test_codegen(page: Page):
    page.goto("https://demoqa.com/")
    page.locator(".card-up").first.click()
    page.get_by_role("listitem").filter(has_text="Text Box").click()
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Alex Dalingo")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("al3927@gmail.com")
    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").fill("18, Nova st, London")
    page.locator("#permanentAddress").click()
    page.locator("#permanentAddress").fill("193, Balashov st, Moscow")
    page.get_by_role("button", name="Submit").click()
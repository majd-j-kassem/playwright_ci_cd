from playwright.sync_api import Page, expect

import pytest

BASE_URL = "http://127.0.0.1:8000/"
NUMBER = 3
RESULT = 27
EMPTY_INPUT_MESSAGE = "Enter a number"

def test_cubic_functionality(page: Page):
    page.goto(BASE_URL)
    input_field = page.get_by_placeholder("Enter a number")
    calculate_button = page.get_by_role("button", name="Cube")
    result_label = page.locator("div#result")
    
    input_field.fill(str(NUMBER))
    calculate_button.click()

    expect(result_label).to_contain_text(str(RESULT))

    
def test_empty_input(page: Page):
    page.goto(BASE_URL)
    input_field = page.get_by_placeholder("Enter a number")
    calculate_button = page.get_by_role("button", name="Cube")
    result_label = page.locator("div#result")
        
    input_field.fill("")
    calculate_button.click()
    
    expect(result_label).to_contain_text(str(EMPTY_INPUT_MESSAGE))



    
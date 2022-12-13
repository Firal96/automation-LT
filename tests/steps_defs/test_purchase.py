from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.support.ui import WebDriverWait

from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.checkout_complete import CheckoutCompletePage

@scenario('purchase.feature', 'Complete the purchase')
def test_purchase():
    pass


@given("the user is in the home page")
def home_page(browser):
    LoginPage(browser).load()

@when(parsers.parse('the user logins as "{user_type}"'))
def login(browser, user_type):
    if user_type == "standard user":
        LoginPage(browser).fill_login("standard_user", "secret_sauce")

@when('the user selects an item', target_fixture="item_name")
def select_item(browser):
    return InventoryPage(browser).select_random_item()

@when('the user clicks in the cart button')
def go_to_cart(browser):
    InventoryPage(browser).click_cart()

@when('the user clicks in the checkout button')
def go_to_checkout(browser):
    CartPage(browser).click_checkout_button()

@when(parsers.parse('the user inputs "{first_name}" in the first name field'))
def fill_first_name(browser, first_name):
    CheckoutPage(browser).fill_name(first_name)

@when(parsers.parse('the user inputs "{last_name}" in the last name field'))
def fill_last_name(browser, last_name):
    CheckoutPage(browser).fill_last_name(last_name)

@when(parsers.parse('the user inputs "{zip}" in the zip field'))
def fill_zip(browser, zip):
    CheckoutPage(browser).fill_zip(zip)

@when('the user clicks in the continue button')
def go_to_overview(browser):
    CheckoutPage(browser).click_continue_button()

@when('the user clicks in the finish button')
def go_to_checkout_complete(browser):
    CheckoutPage(browser).click_finish_button()

@then('the user sees the item in the cart matches the one selected')
def validate_item(browser, item_name):
    assert CartPage(browser).get_item_name() == item_name

@then('the user sees the item in the checkout matches the one selected')
def validate_item_checkout(browser, item_name):
    assert CheckoutPage(browser).get_item_name() == item_name

@then('validate the text order is completed succesfully')
def validate_title(browser):
    assert CheckoutCompletePage(browser).get_title_label() == "CHECKOUT: COMPLETE!"
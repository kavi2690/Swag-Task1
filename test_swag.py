import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from config import BASE_URL, EMAIL, PASSWORD


@pytest.mark.parametrize("sort_option", ["lohi","hilo", "az"])
def test_filter_and_add_to_cart(page, sort_option):

    login = LoginPage(page)
    home = HomePage(page)

    # ---------------- LOGIN ----------------
    login.open(BASE_URL)
    login.enter_email(EMAIL)
    login.enter_password(PASSWORD)
    login.click_login()

    # VERIFY LOGIN SUCCESS
    login.verify_logo()

    # WAIT FOR INVENTORY PAGE (IMPORTANT FIX)
    page.wait_for_url("**/inventory.html")

    print(" Login successful, inventory page loaded")

    # ---------------- SORT PRODUCTS ----------------
    home.sort_products(sort_option)

    print(f" Sorted products by: {sort_option}")

    # Capture first product after sorting
    name, price = home.get_first_product()

    print(f" Selected Product: {name} | {price}")

    # Add product
    home.add_first_product_to_cart()

    print(" Product added to cart")

    # Open cart
    home.open_cart()

    print(" Cart opened")

    # Verify cart
    home.verify_cart(name, price)

    print(f" Test completed for sort option: {sort_option}")
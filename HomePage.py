class HomePage:

    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(5000)

        self.sort_dropdown = page.locator("[data-test='product-sort-container']",)
        
        self.product_names = page.locator("[data-test='inventory-item-name']")
        self.product_prices = page.locator("[data-test='inventory-item-price']")
        self.products = page.locator("[data-test='inventory-item']")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

        print(" HomePage initialized")

    # ---------------- SORT ----------------
    def sort_products(self, option):

        self.sort_dropdown.select_option(option)
        self.page.wait_for_timeout(5000)

        print(f"✅ Products sorted by option: {option}")

    # ---------------- FIRST PRODUCT ----------------
    def get_first_product(self):
        self.page.set_default_timeout(2000)
        name = self.product_names.first.text_content()
        self.page.set_default_timeout(2000)
        price = self.product_prices.first.text_content()

        print(f"📦 First product name: {name}")
        print(f"💰 First product price: {price}")

        return name, price

    # ---------------- ADD PRODUCT ----------------
    def add_first_product_to_cart(self):
        self.page.set_default_timeout(2000)
        self.products.first.locator("button").click()
        self.page.set_default_timeout(2000)
        self.page.wait_for_selector("[data-test='shopping-cart-badge']")

        cart_count = self.cart_badge.text_content()

        print(f"🛒 Product added to cart. Cart count: {cart_count}")

        assert cart_count == "1", "Cart count mismatch"

    # ---------------- OPEN CART ----------------
    def open_cart(self):
        self.page.set_default_timeout(2000)
        self.cart_icon.click()
        self.page.wait_for_url("**/cart.html")

        print("🛍️ Cart page opened successfully")

    # ---------------- VERIFY CART ----------------
    def verify_cart(self, expected_name, expected_price):

        actual_name = self.page.locator("[data-test='inventory-item-name']").first.text_content()
        actual_price = self.page.locator("[data-test='inventory-item-price']").first.text_content()
        actual_qty = self.page.locator("[data-test='item-quantity']").first.text_content()

        print("🔍 Verifying cart details...")
        print(f"✔ Expected Name: {expected_name} | Actual: {actual_name}")
        print(f"✔ Expected Price: {expected_price} | Actual: {actual_price}")
        print(f"✔ Quantity: {actual_qty}")

        assert actual_name == expected_name, "Name mismatch"
        assert actual_price == expected_price, "Price mismatch"
        assert actual_qty == "1", "Quantity mismatch"

        print(" Cart verification successful")
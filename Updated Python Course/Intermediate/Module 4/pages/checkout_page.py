from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_nav = page.locator('[data-test="nav-cart"]')
        self.product_quantity = page.locator('[data-test="product-quantity"]')
        self.proceed_1 = page.locator('[data-test="proceed-1"]')        
        self.continue_as_guest_tab = page.get_by_role("tab", name="Continue as Guest")
        self.guest_email = page.locator('[data-test="guest-email"]')
        self.guest_first_name = page.locator('[data-test="guest-first-name"]')
        self.guest_last_name = page.locator('[data-test="guest-last-name"]')
        self.guest_submit = page.locator('[data-test="guest-submit"]')
        self.proceed_2_guest = page.locator('[data-test="proceed-2-guest"]')
        self.street = page.locator('[data-test="street"]')
        self.city = page.locator('[data-test="city"]')
        self.state = page.locator('[data-test="state"]')
        self.country = page.locator('[data-test="country"]')
        self.postal_code = page.locator('[data-test="postal_code"]')
        self.proceed_3 = page.locator('[data-test="proceed-3"]')
        self.payment_method = page.locator('[data-test="payment-method"]')
        self.finish = page.locator('[data-test="finish"]')
        self.payment_success_message = page.locator('[data-test="payment-success-message"]')
        self.thanks_message = page.get_by_text("Thanks for your order!")

    def open_cart(self):
        self.product_nav.click()

    def update_quantity(self, quantity: int):
        self.product_quantity.click()
        self.product_quantity.fill(str(quantity))

    def proceed_to_checkout(self):
        self.proceed_1.click()

    def fill_guest_info(self, email, first, last):
        self.continue_as_guest_tab.click()
        self.guest_email.fill(email)
        self.guest_first_name.fill(first)
        self.guest_last_name.fill(last)
        self.guest_submit.click()
        self.proceed_2_guest.click()

    def fill_address(self, street, city, state, country, postal_code):
        self.street.fill(street)
        self.city.fill(city)
        self.state.fill(state)
        self.country.fill(country)
        self.postal_code.fill(postal_code)
        self.proceed_3.click()

    def pay_cash_on_delivery(self):
        self.payment_method.select_option('cash-on-delivery')
        self.finish.click()

    def payment_success_message(self):
        return self.payment_success_message

    def click_finish(self):
        self.finish.click()

    def thanks_message(self):
        return self.thanks_message
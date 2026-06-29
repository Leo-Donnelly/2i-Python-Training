from playwright.sync_api import Page

class ProductPage:

    def __init__(self, page: Page):

        self.page = page

        self.add_to_cart = page.locator(
            '[data-test="add-to-cart"]'
        )

    def add_product_to_cart(self):
        self.add_to_cart.click()
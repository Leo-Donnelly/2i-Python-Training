from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):

        self.page = page

        self.categories = page.locator('[data-test="nav-categories"]')
        self.hand_tools = page.locator('[data-test="nav-hand-tools"]')

    def goto(self):
        self.page.goto()("https://practicesoftwaretesting.com")

    def open_hand_tools(self):
        self.categories.click()
        self.hand_tools.click()

    def select_product(self, product_name):

        self.page.get_by_text(
            product_name,
            exact=True
        ).click()
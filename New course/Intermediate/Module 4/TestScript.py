import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize(
    "product_name, quantity",
    [
        ("Claw Hammer", 5),
        ("Combination Pliers", 2),
        ("Thor Hammer", 1),
    ]
)
def test_buy_duplicate_products(home, product, checkout, product_name, quantity):
    home.goto()
    home.sign_in.click()
    home.open_hand_tools()
    home.select_product(product_name)

    product.add_product_to_cart()

    checkout.open_cart()
    checkout.update_quantity(quantity)
    checkout.proceed_to_checkout()

    checkout.fill_guest_info("example@example.com", "Test", "Test")
    checkout.fill_address("Test Street", "Test City", "Test State", "Test Country", "L1 1AA")

    checkout.pay_cash_on_delivery()
    
    expect(checkout.payment_success_message).to_be_visible()
    checkout.click_finish()
    expect(checkout.thanks_message).to_be_visible()
import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def home(page):
    return HomePage(page)

@pytest.fixture
def product(page):
    return ProductPage(page)

@pytest.fixture
def checkout(page):
    return CheckoutPage(page)
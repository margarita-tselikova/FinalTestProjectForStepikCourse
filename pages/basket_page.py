from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty_message(self):
        assert True == self.is_element_present(*BasketPageLocators.BASKET_PAGE_DESCRIPTION), 'Basket is not empty'

    def basket_do_not_have_items(self):
        assert True == self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket has element(s)'

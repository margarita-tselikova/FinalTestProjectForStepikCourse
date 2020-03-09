from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def test_guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        title_in_alert = self.browser.find_element(*ProductPageLocators.TITLE_IN_ALERT).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert title_in_alert == book_title, "Product isn't in basket"
        assert basket_price == book_price, "Basket price isn't match with book price"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.test_guest_can_add_product_to_basket()
        assert True == self.is_not_element_present(*ProductPageLocators.TITLE_IN_ALERT), 'Successful message is on the page for guest user'

    def test_guest_cant_see_success_message(self):
        assert True == self.is_not_element_present(*ProductPageLocators.TITLE_IN_ALERT), 'Successful message is on product page'

    def test_message_disappeared_after_adding_product_to_basket(self):
        self.test_guest_can_add_product_to_basket()
        assert True == self.is_disappeared(*ProductPageLocators.TITLE_IN_ALERT), "Success message don't disappeared"

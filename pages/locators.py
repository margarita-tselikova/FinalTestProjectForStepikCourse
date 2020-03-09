from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR,'button.btn-add-to-basket')
    BOOK_TITLE = (By.CSS_SELECTOR, 'div h1')
    TITLE_IN_ALERT = (By.CSS_SELECTOR, '#messages div.alert-success:nth-child(1) div strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages div.alert-safe:nth-child(3) p strong')
    BOOK_PRICE = (By.CSS_SELECTOR, 'div p.price_color')
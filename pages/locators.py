from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD_CHECK_FIELD = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name = 'registration_submit']")


class ProductPageLocators:
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR,'button.btn-add-to-basket')
    BOOK_TITLE = (By.CSS_SELECTOR, 'div h1')
    TITLE_IN_ALERT = (By.CSS_SELECTOR, '#messages div.alert-success:nth-child(1) div strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages div.alert-safe:nth-child(3) p strong')
    BOOK_PRICE = (By.CSS_SELECTOR, 'div p.price_color')


class BasketPageLocators:
    BASKET_PAGE_DESCRIPTION = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
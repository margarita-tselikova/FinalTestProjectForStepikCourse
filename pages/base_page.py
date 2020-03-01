#   Базовая страница, от которой будут унаследованы все остальные классы.
#   Для описания вспомогательных методов работы с драйвером.

class BasePage():
    def __init__(self, browser,url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
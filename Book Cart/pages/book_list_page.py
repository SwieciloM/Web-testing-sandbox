from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class BookListPage(BasePage):
    """Main page with the list of books in the store."""

    __url = "https://bookcart.azurewebsites.net/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        """Open the main page in the browser."""
        super()._open_url(self.__url)

    def open_book_detail(self, book_title: str):
        pass

    def open_cart(self):
        pass

    def add_book_to_cart(self, book_title: str):
        pass

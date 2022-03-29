import time


class API:
    api_menu = "i"
    api_admin = "text=Admin"
    api_button = "text=API"
    api_help = "i[title='Help']"

    @staticmethod
    def click_api_menu(page):
        page.click(API.api_menu)

    @staticmethod
    def click_api_admin(page):
        page.click(API.api_admin)

    @staticmethod
    def click_api_button(page):
        page.click(API.api_button)

    @staticmethod
    def click_api_help(page):
        page.click(API.api_help)
        page.bring_to_front()

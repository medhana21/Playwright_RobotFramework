import time


class Security:
    security_menu = "i"
    security_Button = "text=Security"
    search_security = "[placeholder=\"Search\"]"
    security_download = ".fa.fa-download.fa-lg"
    security_help = "i[title='Help']"
    security_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[2]"

    @staticmethod
    def click_security_menu(page):
        page.click(Security.security_menu)

    @staticmethod
    def click_security(page):
        page.click(Security.security_Button)
        time.sleep(3)

    @staticmethod
    def click_security_help(page):
        page.click(Security.security_help)
        page.bring_to_front()

    @staticmethod
    def click_security_search(page):
        page.click(Security.search_security)

    @staticmethod
    def enter_security_search(page, policy):
        page.fill(Security.search_security, policy)

    @staticmethod
    def click_security_download(page):
        page.click(Security.security_download)
        time.sleep(5)

    @staticmethod
    def click_security_ui_setting(page):
        page.click(Security.security_ui_setting)

import time


class Savings:
    saving_menu = "i"
    saving_Button = "text=Savings"
    search_saving = "[placeholder=\"Search\"]"
    saving_download = ".fa.fa-download.fa-lg"
    saving_help = "i[title='Help']"
    saving_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_savings_menu(page):
        page.click(Savings.saving_menu)

    @staticmethod
    def click_savings(page):
        page.click(Savings.saving_Button)
        time.sleep(3)

    @staticmethod
    def click_savings_help(page):
        page.click(Savings.saving_help)
        page.bring_to_front()

    @staticmethod
    def click_savings_search(page):
        page.click(Savings.search_saving)

    @staticmethod
    def enter_savings_search(page, policy):
        page.fill(Savings.search_saving, policy)

    @staticmethod
    def click_savings_download(page):
        page.click(Savings.saving_download)
        time.sleep(5)

    @staticmethod
    def click_savings_ui_setting(page):
        page.click(Savings.saving_ui_setting)

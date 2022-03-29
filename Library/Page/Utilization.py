import time


class Utilization:
    utilization_menu = "i"
    ri_button = "text = Reserved Instance"
    utilization_button = "text=Utilization"
    search_utilization = "[placeholder=\"Search\"]"
    utilization_download = ".fa.fa-download.fa-lg"
    utilization_help = "i[title='Help']"
    utilization_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_utilization_menu(page):
        page.click(Utilization.utilization_menu)


    @staticmethod
    def click_ri_button(page):
        page.click(Utilization.ri_button)

    @staticmethod
    def click_utilization(page):
        page.click(Utilization.utilization_button)
        time.sleep(3)

    @staticmethod
    def click_utilization_help(page):
        page.click(Utilization.utilization_help)
        page.bring_to_front()

    @staticmethod
    def click_utilization_search(page):
        page.click(Utilization.search_utilization)

    @staticmethod
    def enter_utilization_search(page, ser_name):
        page.fill(Utilization.search_utilization, ser_name)

    @staticmethod
    def click_utilization_download(page):
        page.click(Utilization.utilization_download)
        time.sleep(5)

    @staticmethod
    def click_utilization_ui_setting(page):
        page.click(Utilization.utilization_ui_setting)

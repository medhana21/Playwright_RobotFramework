import time


class Resource:
    menu = "i"
    resource_Button = "text=Resources"
    search_resource = "[placeholder=\"Search\"]"
    resource_download = ".fa.fa-download.fa-lg"
    r_help = "i[title='Help']"
    r_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_resource_menu(page):
        page.click(Resource.menu)

    @staticmethod
    def click_resource(page):
        page.click(Resource.resource_Button)
        time.sleep(3)

    @staticmethod
    def click_resource_help(page):
        page.click(Resource.r_help)
        page.bring_to_front()

    @staticmethod
    def click_resource_search(page):
        page.click(Resource.search_resource)

    @staticmethod
    def enter_resource_search(page, res):
        page.fill(Resource.search_resource, res)

    @staticmethod
    def click_resource_download(page):
        page.click(Resource.resource_download)
        time.sleep(5)

    @staticmethod
    def click_resource_ui_setting(page):
        page.click(Resource.r_ui_setting)
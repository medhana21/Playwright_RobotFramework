import time


class Coverage:
    coverage_menu = "i"
    ri = "text = Reserved Instance"
    coverage_button = "//button[@class='btn btn-link'][normalize-space()='Coverage']"
    search_coverage = "[placeholder=\"Search\"]"
    coverage_download = ".fa.fa-download.fa-lg"
    coverage_help = "i[title='Help']"
    coverage_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_coverage_menu(page):
        page.click(Coverage.coverage_menu)

    @staticmethod
    def click_ri(page):
        page.click(Coverage.ri)

    @staticmethod
    def click_on_coverage_button(page):
        page.click(Coverage.coverage_button)

    @staticmethod
    def click_coverage_help(page):
        page.click(Coverage.coverage_help)
        page.bring_to_front()

    @staticmethod
    def click_coverage_search(page):
        page.click(Coverage.search_coverage)

    @staticmethod
    def enter_coverage_search(page, platform):
        page.fill(Coverage.search_coverage, platform)

    @staticmethod
    def click_coverage_download(page):
        page.click(Coverage.coverage_download)
        time.sleep(5)

    @staticmethod
    def click_coverage_ui_setting(page):
        page.click(Coverage.coverage_ui_setting)

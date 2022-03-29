import time


class Compliance:
    compliance_menu = "i"
    compliance_Button = "text=Compliance"
    search_compliance = "[placeholder=\"Search\"]"
    compliance_download = ".fa.fa-download.fa-lg"
    compliance_help = "i[title='Help']"
    compliance_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[2]"

    @staticmethod
    def click_compliance_menu(page):
        page.click(Compliance.compliance_menu)

    @staticmethod
    def click_compliance(page):
        page.click(Compliance.compliance_Button)
        time.sleep(3)

    @staticmethod
    def click_compliance_help(page):
        page.click(Compliance.compliance_help)
        page.bring_to_front()

    @staticmethod
    def click_compliance_search(page):
        page.click(Compliance.search_compliance)

    @staticmethod
    def enter_compliance_search(page, policy):
        page.fill(Compliance.search_compliance, policy)

    @staticmethod
    def click_compliance_download(page):
        page.click(Compliance.compliance_download)
        time.sleep(5)

    @staticmethod
    def click_compliance_ui_setting(page):
        page.click(Compliance.compliance_ui_setting)

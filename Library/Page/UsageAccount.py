import time


class UsageAccount:
    usage_menu = "i"
    usage_admin = "text=Admin"
    usage_button = "text=Usage Account"
    u_help = "i[title='Help']"
    create_usage_ac = "//button[@type='button']"
    u_manual = "(//a[normalize-space()='Manual'])[1]"
    u_gcp = "//img[@src='/assets/images/gcp.svg']"
    u_cancel = "(//button[normalize-space()='Cancel'])[1]"
    aws_usage_edit = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/usage-account[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[1]/datatable-body-row[1]/div[2]/datatable-body-cell[7]/div[1]/a[1]/i[1]"
    aws_usage_delete = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/usage-account[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[1]/datatable-body-row[1]/div[2]/datatable-body-cell[7]/div[1]/a[2]/i[1]"
    search_usage_ac = "[placeholder=\"Search\"]"
    usage_ac_download = ".fa.fa-download.fa-lg"
    usage_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_usage_menu(page):
        page.click(UsageAccount.usage_menu)

    @staticmethod
    def click_usage_admin(page):
        page.click(UsageAccount.usage_admin)

    @staticmethod
    def click_usage_button(page):
        page.click(UsageAccount.usage_button)

    @staticmethod
    def click_usage_help(page):
        page.click(UsageAccount.u_help)
        page.bring_to_front()

    @staticmethod
    def click_create_usage_ac(page):
        page.click(UsageAccount.create_usage_ac)

    @staticmethod
    def click_u_manual(page):
        page.click(UsageAccount.u_manual)

    @staticmethod
    def click_gcp_usage(page):
        page.click(UsageAccount.u_gcp)

    @staticmethod
    def click_cancel_usage(page):
        page.click(UsageAccount.u_cancel)

    @staticmethod
    def click_edit_usage(page):
        page.click(UsageAccount.aws_usage_edit)
        page.click(UsageAccount.u_cancel)

    @staticmethod
    def click_delete_usage(page):
        page.click(UsageAccount.aws_usage_delete)
        page.click(UsageAccount.u_cancel)

    @staticmethod
    def click_search_usage_ac(page):
        page.click(UsageAccount.search_usage_ac)

    @staticmethod
    def fill_search_usage_ac(page, search_usage_ac):
        page.fill(UsageAccount.search_usage_ac, search_usage_ac)

    @staticmethod
    def click_usage_ac_download(page):
        page.click(UsageAccount.usage_ac_download)

    @staticmethod
    def click_usage_ui_setting(page):
        page.click(UsageAccount.usage_ui_setting)
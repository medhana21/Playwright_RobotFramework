import time


class BillingAccount:
    billing_menu = "i"
    billing_admin = "text=Admin"
    billing_button = "text=Billing Account"
    b_help = "i[title='Help']"
    create_billing_ac = "//button[@type='button']"
    cloudformation = "(//a[normalize-space()='CloudFormation'])[1]"
    gcp = "//img[@src='/assets/images/gcp.svg']"
    cancel = "(//button[normalize-space()='Cancel'])[1]"
    aws_billing_edit = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/account[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[1]/datatable-body-row[1]/div[2]/datatable-body-cell[8]/div[1]/a[1]/i[1]"
    aws_billing_delete = "(//i[@aria-hidden='true'])[12]"
    search_billing_ac = "[placeholder=\"Search\"]"
    billing_ac_download = ".fa.fa-download.fa-lg"
    b_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_billing_menu(page):
        page.click(BillingAccount.billing_menu)

    @staticmethod
    def click_billing_admin(page):
        page.click(BillingAccount.billing_admin)

    @staticmethod
    def click_billing_button(page):
        page.click(BillingAccount.billing_button)

    @staticmethod
    def click_billing_help(page):
        page.click(BillingAccount.b_help)
        page.bring_to_front()

    @staticmethod
    def click_create_billing_ac(page):
        page.click(BillingAccount.create_billing_ac)

    @staticmethod
    def click_cloudformation(page):
        page.click(BillingAccount.cloudformation)

    @staticmethod
    def click_gcp_billing(page):
        page.click(BillingAccount.gcp)

    @staticmethod
    def click_cancel_billing(page):
        page.click(BillingAccount.cancel)

    @staticmethod
    def click_edit_billing(page):
        page.click(BillingAccount.aws_billing_edit)
        page.click(BillingAccount.cancel)

    @staticmethod
    def click_delete_billing(page):
        page.click(BillingAccount.aws_billing_delete)
        page.click(BillingAccount.cancel)

    @staticmethod
    def click_search_billing_ac(page):
        page.click(BillingAccount.search_billing_ac)

    @staticmethod
    def fill_search_billing_ac(page, search_billing_ac):
        page.fill(BillingAccount.search_billing_ac, search_billing_ac)

    @staticmethod
    def click_billing_ac_download(page):
        page.click(BillingAccount.billing_ac_download)

    @staticmethod
    def click_billing_ui_setting(page):
        page.click(BillingAccount.b_ui_setting)



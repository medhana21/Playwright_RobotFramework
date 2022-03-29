import time


class Integration:
    menu = "i"
    admin = "text=Admin"
    integration_module = "text=Integrations"
    i_help = "i[title='Help']"
    create_integration = "text=Create Integration"
    name = "//input[@name='s-name']"
    desc = "//input[@name='description']"
    app = "(//div[@class='ngx-select__toggle btn form-control'])[1]"
    slack = "//span[@class='ng-star-inserted'][normalize-space()='Slack']"
    type = "(//div[@class='ngx-select__toggle btn form-control'])[2]"
    webhook = "//span[normalize-space()='Webhook']"
    address= "//textarea[@name='address']"
    submit = "//span[normalize-space()='Create']"
    edit_integration = "body > app-root:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > integration:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > mcx-table:nth-child(1) > div:nth-child(1) > ngx-datatable:nth-child(2) > div:nth-child(1) > datatable-body:nth-child(2) > datatable-selection:nth-child(2) > datatable-scroller:nth-child(1) > datatable-row-wrapper:nth-child(7) > datatable-body-row:nth-child(1) > div:nth-child(2) > datatable-body-cell:nth-child(7) > div:nth-child(1) > a:nth-child(1) > i:nth-child(1)"
    cancel_edit_integration = "text=Cancel"
    delete_integration = "body > app-root:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > integration:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > mcx-table:nth-child(1) > div:nth-child(1) > ngx-datatable:nth-child(2) > div:nth-child(1) > datatable-body:nth-child(2) > datatable-selection:nth-child(2) > datatable-scroller:nth-child(1) > datatable-row-wrapper:nth-child(7) > datatable-body-row:nth-child(1) > div:nth-child(2) > datatable-body-cell:nth-child(7) > div:nth-child(1) > a:nth-child(2) > i:nth-child(1)"
    cancel_delete_integration = "text=Cancel"
    search_integration = "[placeholder=\"Search\"]"
    integration_download = ".fa.fa-download.fa-lg"
    i_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_integration_menu(page):
        page.click(Integration.menu)
        time.sleep(3)

    @staticmethod
    def click_integration_admin(page):
        page.click(Integration.admin)

    @staticmethod
    def click_integration_module(page):
        page.click(Integration.integration_module)

    @staticmethod
    def click_integration_help(page):
        page.click(Integration.i_help)
        page.bring_to_front()

    @staticmethod
    def click_create_integration(page):
        page.click(Integration.create_integration)

    @staticmethod
    def click_integration_name(page):
        page.click(Integration.name)

    @staticmethod
    def fill_integration_name(page, name):
        page.fill(Integration.name, name)

    @staticmethod
    def click_integration_desc(page):
        page.click(Integration.desc)

    @staticmethod
    def fill_integration_desc(page, desc):
        page.fill(Integration.desc, desc)

    @staticmethod
    def click_app(page):
        page.click(Integration.app)

    @staticmethod
    def select_slack(page):
        page.click(Integration.slack)

    @staticmethod
    def click_type(page):
        page.click(Integration.type)

    @staticmethod
    def select_webhook(page):
        page.click(Integration.webhook)

    @staticmethod
    def click_address(page):
        page.click(Integration.address)

    @staticmethod
    def fill_address(page,add):
        page.fill(Integration.address,add)

    @staticmethod
    def  click_i_create(page):
        page.click(Integration.submit)

    @staticmethod
    def click_edit_integration(page):
        page.click(Integration.edit_integration)

    @staticmethod
    def click_cancel_edit_integration(page):
        page.click(Integration.cancel_edit_integration)

    @staticmethod
    def click_delete_integration(page):
        page.click(Integration.delete_integration)

    @staticmethod
    def click_cancel_delete_integration(page):
        page.click(Integration.cancel_delete_integration)

    @staticmethod
    def click_integration_search(page):
        page.click(Integration.search_integration)

    @staticmethod
    def fill_integration_search(page, i):
        page.fill(Integration.search_integration, i)

    @staticmethod
    def click_integration_download(page):
        page.click(Integration.integration_download)
        time.sleep(2)

    @staticmethod
    def click_integration_ui_setting(page):
        page.click(Integration.i_ui_setting)



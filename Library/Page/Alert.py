import time


class Alert:
    menu = "i"
    admin = "text=Admin"
    alerts_page = "text=Alerts"
    alert_help = "i[title='Help']"
    create_alert = "text=Create Alert"
    alert_rule = "ngx-select >> text=Monthly cost"
    daily_cost = "ul[role=\"menu\"] >> text=Daily cost"
    provider = "form >> text=of provider"
    of_provider = "li[role=\"menuitem\"] >> text=of provider"
    select = "text=Select"
    aws = "ng-multiselect-dropdown >> text=aws"
    c_dropdown = "label[for='rule']"
    is_more_than = "form >> text=is more than"
    is_going_up_by = "ul[role=\"menu\"] >> text=is going up by"
    cost = "input[name=\"threshold\"]"
    notify_user = "ng-multiselect-dropdown[name='users'] div span[class='ng-star-inserted']"
    userid = "text=abdul.khader+automation@mindsnxt.com"
    close_n = "text=Notify Users"
    notify_ch = "text=Select"
    sel_ch = "(//div[contains(text(),'Slack Webhook')])[1]"
    create = "text=Create Cancel >> button"
    edit = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/app-alert[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[2]/datatable-body-row[1]/div[2]/datatable-body-cell[6]/div[1]/a[1]/i[1]"
    cancel = ".btn.btn-light"
    delete = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/app-alert[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[2]/datatable-body-row[1]/div[2]/datatable-body-cell[6]/div[1]/a[2]/i[1]"
    d_cancel = "text=Cancel"
    search = "input[placeholder='Search']"
    alert_download = ".fa.fa-download.fa-lg"
    a_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_alert_menu(page):
        page.click(Alert.menu)

    @staticmethod
    def click_alert_admin(page):
        page.click(Alert.admin)

    @staticmethod
    def click_on_alerts(page):
        page.click(Alert.alerts_page)

    @staticmethod
    def click_alert_help(page):
        page.click(Alert.alert_help)
        page.bring_to_front()

    @staticmethod
    def click_create_alert(page):
        page.click(Alert.create_alert)

    @staticmethod
    def click_alert_rule(page):
        page.click(Alert.alert_rule)

    @staticmethod
    def click_daily_cost(page):
        page.click(Alert.daily_cost)

    @staticmethod
    def click_provider(page):
        page.click(Alert.provider)

    @staticmethod
    def click_of_provider(page):
        page.click(Alert.of_provider)

    @staticmethod
    def click_select_drop(page):
        page.click(Alert.select)

    @staticmethod
    def click_gcp(page):
        page.click(Alert.aws)

    @staticmethod
    def click_close_dropdown(page):
        page.click(Alert.c_dropdown)

    @staticmethod
    def click_is_more_than(page):
        page.click(Alert.is_more_than)

    @staticmethod
    def click_is_going_up_by(page):
        page.click(Alert.is_going_up_by)

    @staticmethod
    def click_send_cost(page):
        page.click(Alert.cost)

    @staticmethod
    def send_cost(page, c):
        page.fill(Alert.cost, c)

    @staticmethod
    def click_notify_user(page):
        page.click(Alert.notify_user)

    @staticmethod
    def click_user_id(page):
        page.click(Alert.userid)

    @staticmethod
    def close_notify(page):
        page.click(Alert.close_n)

    @staticmethod
    def click_notify_ch(page):
        page.click(Alert.notify_ch)

    @staticmethod
    def click_sel_ch(page):
        page.click(Alert.sel_ch)

    @staticmethod
    def click_create(page):
        page.click(Alert.create)

    @staticmethod
    def click_edit(page):
        page.click(Alert.edit)

    @staticmethod
    def click_cancel(page):
        page.click(Alert.cancel)

    @staticmethod
    def click_delete(page):
        page.click(Alert.delete)

    @staticmethod
    def click_d_cancel(page):
        page.click(Alert.d_cancel)

    @staticmethod
    def click_search(page):
        page.click(Alert.search)

    @staticmethod
    def enter_to_search(page, search):
        page.fill(Alert.search, search)

    @staticmethod
    def click_alert_download(page):
        page.click(Alert.alert_download)
        time.sleep(2)

    @staticmethod
    def click_alert_ui_setting(page):
        page.click(Alert.a_ui_setting)

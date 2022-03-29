import time


class Costs:
    c_menu = "i"
    cost_Button = "text=Cost"
    cost_help = "text=Help"
    cost_share = "//i[@title='Share']"
    cost_bookmark = "//i[@title='Bookmark']"
    cost_b_name = "//input[@name='b-name']"
    cost_b_desc = "//input[@name='description']"
    select_c_b_user = "//span[contains(text(),'Select')]"
    c_b_user = "//div[normalize-space()='abdul.khader+automation@mindsnxt.com']"
    c_b_fav = "//i[@class='fa-lg fa-star far']"
    c_b_create = "//span[normalize-space()='Create']"
    cost_subscription = "//i[@title='Subscription']"
    cost_sub_name = "//input[@name='s-name']"
    cost_sub_desc = "//input[@name='description']"
    cost_sub_create = "//span[normalize-space()='Create']"
    cost_screenshot = "//i[@title='Screenshot']"
    cost_filter = "//i[@title='Filters']"
    select_cost_usage = "(//span[@class='ng-star-inserted'][normalize-space()='Select'])[3]"
    select_cloudwiz = "(//div[contains(text(),'cloudwiz')])[2]"
    apply_cost_filter = "//button[@class='btn btn-primary']"
    cost_info = "//i[@title='Info']"
    cost_reload = "//i[@title='Reload']"
    search_cost = "[placeholder=\"Search\"]"
    cost_download = ".fa.fa-download.fa-lg"
    c_help = "i[title='Help']"
    c_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_c_menu(page):
        page.click(Costs.c_menu)

    @staticmethod
    def click_cost(page):
        page.click(Costs.cost_Button)
        time.sleep(3)

    @staticmethod
    def click_cost_help(page):
        page.click(Costs.c_help)
        page.bring_to_front()

    @staticmethod
    def click_cost_share(page):
        page.click(Costs.cost_share)

    @staticmethod
    def click_cost_bookmark(page):
        page.click(Costs.cost_bookmark)

    @staticmethod
    def enter_cost_b_name(page, c_b_name):
        page.fill(Costs.cost_b_name, c_b_name)

    @staticmethod
    def enter_cost_b_desc(page, c_b_desc):
        page.fill(Costs.cost_b_desc, c_b_desc)

    @staticmethod
    def select_cost_b_user(page):
        page.click(Costs.select_c_b_user)

    @staticmethod
    def cost_b_user(page):
        page.click(Costs.c_b_user)
        page.click(Costs.cost_b_name)

    @staticmethod
    def cost_b_fav(page):
        page.click(Costs.c_b_fav)

    @staticmethod
    def cost_b_create(page):
        page.click(Costs.c_b_create)

    @staticmethod
    def click_cost_subscription(page):
        page.click(Costs.cost_subscription)

    @staticmethod
    def enter_cost_sub_name(page, c_s_name):
        page.fill(Costs.cost_sub_name,  c_s_name)

    @staticmethod
    def enter_cost_sub_desc(page, c_s_desc):
        page.fill(Costs.cost_sub_desc, c_s_desc)

    @staticmethod
    def create_cost_subscription(page):
        page.click(Costs.cost_sub_create)

    @staticmethod
    def click_cost_screenshot(page):
        page.click(Costs.cost_screenshot)

    @staticmethod
    def click_cost_filter(page):
        page.click(Costs.cost_filter)

    @staticmethod
    def select_cost_usage_filter(page):
        page.click(Costs.select_cost_usage)

    @staticmethod
    def select_cost_cloudwiz(page):
        page.click(Costs.select_cloudwiz)

    @staticmethod
    def apply_cost_usage_filter(page):
        page.click(Costs.apply_cost_filter)

    @staticmethod
    def click_cost_info(page):
        page.click(Costs.cost_info)

    @staticmethod
    def click_cost_reload(page):
        page.click(Costs.cost_reload)

    @staticmethod
    def click_cost_search(page):
        page.click(Costs.search_cost)

    @staticmethod
    def enter_cost_search(page, service):
        page.fill(Costs.search_cost, service)

    @staticmethod
    def click_cost_download(page):
        page.click(Costs.cost_download)
        time.sleep(5)

    @staticmethod
    def click_cost_ui_setting(page):
        page.click(Costs.c_ui_setting)

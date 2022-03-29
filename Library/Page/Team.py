import time


class Team:
    menu = "i"
    admin = "text=Admin"
    team_module = "text=Teams"
    t_help = "i[title='Help']"
    create_team = "text=Create Team"
    t_name = "//input[@name='teamname']"
    t_desc = "//input[@name='teamdesc']"
    click_user = "text=Select"
    select_user = "text=abdul.khader+automation@mindsnxt.com"
    accounts = "//input[@name='allAccounts']"
    create = "//span[normalize-space()='Create']"
    edit_team = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/app-team[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[1]/datatable-body-row[1]/div[2]/datatable-body-cell[5]/div[1]/a[1]/i[1]"
    cancel_edit_team = "text=Cancel"
    delete_team = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/app-team[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[1]/datatable-body-row[1]/div[2]/datatable-body-cell[5]/div[1]/a[2]/i[1]"
    cancel_delete_team = "text=Cancel"
    search_team = "[placeholder=\"Search\"]"
    team_download = ".fa.fa-download.fa-lg"
    t_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_team_menu(page):
        page.click(Team.menu)
        time.sleep(3)

    @staticmethod
    def click_team_admin(page):
        page.click(Team.admin)

    @staticmethod
    def click_team_module(page):
        page.click(Team.team_module)

    @staticmethod
    def click_team_help(page):
        page.click(Team.t_help)
        page.bring_to_front()

    @staticmethod
    def click_create_team(page):
        page.click(Team.create_team)

    @staticmethod
    def enter_team_name(page, t_name):
        page.fill(Team.t_name, t_name)

    @staticmethod
    def enter_description(page, t_desc):
        page.fill(Team.t_desc, t_desc)

    @staticmethod
    def click_users(page):
        page.click(Team.click_user)

    @staticmethod
    def select_users(page):
        page.click(Team.select_user)
        page.click(Team.t_name)

    @staticmethod
    def click_accounts(page):
        page.click(Team.accounts)

    @staticmethod
    def click_t_submit(page):
        page.click(Team.create)

    @staticmethod
    def click_edit_team(page):
        page.click(Team.edit_team)

    @staticmethod
    def click_cancel_edit_team(page):
        page.click(Team.cancel_edit_team)

    @staticmethod
    def click_delete_team(page):
        page.click(Team.delete_team)

    @staticmethod
    def click_cancel_delete_team(page):
        page.click(Team.cancel_delete_team)

    @staticmethod
    def click_team_search(page):
        page.click(Team.search_team)

    @staticmethod
    def fill_team_search(page, t):
        page.fill(Team.search_team, t)

    @staticmethod
    def click_team_download(page):
        page.click(Team.team_download)
        time.sleep(2)

    @staticmethod
    def click_team_ui_setting(page):
        page.click(Team.t_ui_setting)


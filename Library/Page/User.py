import time


class User:
    menu = "i"
    admin = "text=Admin"
    user_module = "text=Users"
    u_help = "i[title='Help']"
    create_user = "text=Create User"
    name = "input[name=\"name\"]"
    email_id = "input[name=\"email\"]"
    select_roles = "ng-multiselect-dropdown[name='roles'] div[class='multiselect-dropdown'] div span[class='dropdown-btn']"
    owner = "ng-multiselect-dropdown >> text=Owner"
    administrator = "ng-multiselect-dropdown >> text=Administrator"
    select_team = "//ng-multiselect-dropdown[@name='teams']//div//span[@class='ng-star-inserted'][normalize-space()='Select']"
    team_owner = "form >> text=Team Owner"
    submit = "text=Create Cancel >> button"
    edit_user = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/app-user[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[5]/datatable-body-row[1]/div[2]/datatable-body-cell[6]/div[1]/a[1]/i[1]"
    cancel_edit_user = "text=Cancel"
    delete_user = "//body[1]/app-root[1]/div[1]/div[1]/div[1]/div[1]/app-user[1]/div[1]/section[1]/div[1]/mcx-table[1]/div[1]/ngx-datatable[1]/div[1]/datatable-body[1]/datatable-selection[1]/datatable-scroller[1]/datatable-row-wrapper[5]/datatable-body-row[1]/div[2]/datatable-body-cell[6]/div[1]/a[2]/i[1]"
    cancel_delete_user = "text=Cancel"
    search_user = "[placeholder=\"Search\"]"
    user_download = ".fa.fa-download.fa-lg"
    u_ui_setting = "(//i[@class='fa fa-lg fa-cog'])[1]"

    @staticmethod
    def click_user_menu(page):
        page.click(User.menu)
        time.sleep(3)

    @staticmethod
    def click_admin(page):
        page.click(User.admin)

    @staticmethod
    def click_user_module(page):
        page.click(User.user_module)

    @staticmethod
    def click_user_help(page):
        page.click(User.u_help)
        page.bring_to_front()

    @staticmethod
    def click_create_user(page):
        page.click(User.create_user)

    @staticmethod
    def click_name(page):
        page.click(User.name)

    @staticmethod
    def fill_name(page, name):
        page.fill(User.name, name)

    @staticmethod
    def click_email_id(page):
        page.click(User.email_id)

    @staticmethod
    def fill_email_id(page, email):
        page.fill(User.email_id, email)

    @staticmethod
    def click_select_roles(page):
        page.click(User.select_roles)

    @staticmethod
    def click_owner(page):
        page.click(User.owner)

    @staticmethod
    def click_administrator(page):
        page.click(User.administrator)

    @staticmethod
    def click_select_team(page):
        page.click(User.select_team)

    @staticmethod
    def click_team_owner(page):
        page.click(User.team_owner)

    @staticmethod
    def click_submit(page):
        page.click(User.submit)
        time.sleep(3)

    @staticmethod
    def click_edit_user(page):
        page.click(User.edit_user)

    @staticmethod
    def click_cancel_edit_user(page):
        page.click(User.cancel_edit_user)

    @staticmethod
    def click_delete_user(page):
        page.click(User.delete_user)

    @staticmethod
    def click_cancel_delete_user(page):
        page.click(User.cancel_delete_user)

    @staticmethod
    def click_user_search(page):
        page.click(User.search_user)

    @staticmethod
    def fill_user_search(page, u):
        page.fill(User.search_user, u)

    @staticmethod
    def click_user_download(page):
        page.click(User.user_download)
        time.sleep(2)

    @staticmethod
    def click_user_ui_setting(page):
        page.click(User.u_ui_setting)



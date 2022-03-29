import time


class SSO:
    sso_menu = "i"
    sso_admin = "text=Admin"
    sso_button = "text=SSO"
    sso_help = "i[title='Help']"
    edit = "(//button[normalize-space()='Edit'])[1]"
    cancel = "(//button[normalize-space()='Cancel'])[1]"
    delete = "(//button[normalize-space()='Delete'])[1]"
    no = "(//a[normalize-space()='No'])[1]"

    @staticmethod
    def click_sso_menu(page):
        page.click(SSO.sso_menu)

    @staticmethod
    def click_sso_admin(page):
        page.click(SSO.sso_admin)

    @staticmethod
    def click_sso_button(page):
        page.click(SSO.sso_button)

    @staticmethod
    def click_sso_help(page):
        page.click(SSO.sso_help)
        page.bring_to_front()

    @staticmethod
    def click_sso_edit(page):
        page.click(SSO.edit)

    @staticmethod
    def click_sso_cancel(page):
        page.click(SSO.cancel)

    @staticmethod
    def click_sso_delete(page):
        page.click(SSO.delete)

    @staticmethod
    def click_sso_delete_no(page):
        page.click(SSO.no)

import time
from playwright.sync_api import sync_playwright
import configparser
import os


class PlaywrightCore:
    browser = None
    context = None
    page = None
    pwSync = None

    @staticmethod
    def launch_browser(browser_name='chromium', record_video=True):
        # config = configparser.RawConfigParser()
        # config.read(os.getcwd() + "/config.txt")

        # browser_name = config.get('Browser', 'browser_name')
        # head_less = eval(config.get('Browser', 'head_less'))
        # record_video = eval(config.get('Browser', 'record_video'))
        # slow_mo = int(config.get('Browser', 'head_less'))

        print("Opening Browser : " + browser_name)

        PlaywrightCore.pwSync = sync_playwright().start()  # creating sync obj
        if browser_name.lower() == 'chromium':
            PlaywrightCore.browser = PlaywrightCore.pwSync.chromium.launch(headless=False, slow_mo=1000)
        elif browser_name.lower() == 'firefox':
            PlaywrightCore.browser = PlaywrightCore.pwSync.firefox.launch(headless=False, slow_mo=1000)
        else:
            PlaywrightCore.browser = PlaywrightCore.pwSync.webkit.launch(headless=False, slow_mo=1000)
        if record_video:
            PlaywrightCore.context = PlaywrightCore.browser.new_context(
                viewport={"width": 1375, "height": 885},
                record_video_dir="Videos/",
                record_video_size={"width": 640, "height": 480}
            )
        else:
            PlaywrightCore.context = PlaywrightCore.browser.new_context()

    @staticmethod
    def open_application():
        PlaywrightCore.page = PlaywrightCore.context.new_page()
        PlaywrightCore.page.goto("https://mindsnxt.cloudwiz.xyz/cost")

    @staticmethod
    def login_application():
        PlaywrightCore.page.fill("[placeholder=\"Email\"]", "abdul.khader@mindsnxt.com")
        PlaywrightCore.page.fill("[placeholder=\"Password\"]", "Minds@123")
        PlaywrightCore.page.click("button:has-text(\"Login\")")
        time.sleep(15)

    @staticmethod
    def get_page_object():
        return PlaywrightCore.page

    @staticmethod
    def take_screenshot():
        return PlaywrightCore.page.screenshot(path="Reports/screenshot.png")

    @staticmethod
    def logout_application():
        time.sleep(5)
        PlaywrightCore.page.click("button:has-text(\"Abdul Khader Default Owner\")")
        PlaywrightCore.page.click("text=Logout")

    @staticmethod
    def close_application():
        PlaywrightCore.page.close()

    @staticmethod
    def close_browser():
        PlaywrightCore.context.close()
        PlaywrightCore.browser.close()
        PlaywrightCore.pwSync.stop()

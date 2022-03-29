*** Settings ***
Documentation           Common helper file
Library                 ../PyLib/PlaywrightCore.py
Library                 ../Page/User.py

*** Keywords ***
Launch Browser Engine
    launch browser  browser_name=chromium

Launch Firefox Engine
    launch browser  browser_name=firefox

Launch Webkit Engine
    launch browser  browser_name=webkit

Quit Opened Browser
    close browser

Open Cloudwiz Application
    open application
    login application
    take screenshot


Close Cloudwiz Application
    logout application
    close application

Get Page Handle
    ${page_handle}    get page object
    [Return]    ${page_handle}

*** Settings ***
Documentation           This is a SSO test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
SSO File Test Case
    Log  "This is sso test case"
    SSO.Perform action on SSO


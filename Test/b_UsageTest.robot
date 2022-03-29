*** Settings ***
Documentation           This is a Usage test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
 Usage Account File Test Case
    Log  "This is usage account test case"
    Usage Account.Perform action on Usage Account


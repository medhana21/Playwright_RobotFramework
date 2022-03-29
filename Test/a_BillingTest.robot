*** Settings ***
Documentation           This is a Billing test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
 Billing Account File Test Case
    Log  "This is billing account test case"
    ${search_billing_ac} =      Set Variable         cloudwiz
    Billing Account.Perform action on Billing Account    ${search_billing_ac}


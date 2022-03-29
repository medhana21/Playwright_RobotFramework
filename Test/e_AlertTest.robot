*** Settings ***
Documentation           This is a Alert test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Alerts File Test Case
    Log  "This is Alert test case"
    ${cost} =   Set Variable       3
    ${search} =  Set variable   abdul.khader
    Alerts.Perform action on Alert    ${cost}     ${search}




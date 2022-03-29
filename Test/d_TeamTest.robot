*** Settings ***
Documentation           This is a Team test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Team File Test Case
    Log  "This is user test case"
    ${t_name} =   Set Variable       QA Automation Team
    ${description} =  Set Variable       This is QA Automation Team
    ${team} =   Set Variable  QA Automation Team
    Teams.Get Data from team    ${t_name}     ${description}   ${team}

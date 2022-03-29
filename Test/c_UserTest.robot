*** Settings ***
Documentation           This is a User test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
User File Test Case
    Log  "This is user test case"
    ${name} =   Set Variable       Abdul Automation User
    ${email} =  Set Variable       abdul.khader+automation@mindsnxt.com
    ${user} =   Set Variable       abdul.khader+automation
    Users.Get Data from user    ${name}     ${email}      ${user}

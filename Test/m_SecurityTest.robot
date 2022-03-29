*** Settings ***
Documentation           This is a Security test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Security File Test Case
    Log  "This is security test case"
    ${policy} =  Set Variable       EC2 Unrestricted Security Group
    Security.Perform action on Security  ${policy}


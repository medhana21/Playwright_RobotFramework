*** Settings ***
Documentation           This is a Savings test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Savings File Test Case
    Log  "This is saving test case"
    ${policy} =  Set Variable       EC2 Instance Idle
    Savings.Perform action on Savings   ${policy}


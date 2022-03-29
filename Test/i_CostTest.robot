*** Settings ***
Documentation           This is a Cost test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Costs File Test Case
    Log  "This is cost test case"
    ${c_b_name} =   Set Variable       Automation Cost Bookmark
    ${c_b_desc} =   Set Variable       This is Cost Bookmark
    ${c_s_name} =   Set Variable       Automation Cost Subscription
    ${c_s_desc} =   Set Variable       This is Cost Subscription
    ${service} =   Set Variable       EC2
    Costs.Perform action on Costs  ${c_b_name}   ${c_b_desc}    ${c_s_name}   ${c_s_desc}   ${service}
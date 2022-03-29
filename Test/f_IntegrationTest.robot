*** Settings ***
Documentation           This is a integration test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Integration File Test Case
    Log  "This is user test case"
    ${name} =   Set Variable            Automation Slack Webhook
    ${desc} =  Set Variable             This is Automation Slack Webhook
    ${address} =   Set Variable         https://hooks.slack.com/services/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
    ${integration} =   Set Variable     Automation Slack Webhook
    Integration.Get Data from integration    ${name}     ${desc}       ${address}   ${integration}

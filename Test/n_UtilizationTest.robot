*** Settings ***
Documentation           This is a Utilization test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Utilization File Test Case
    Log  "This is saving test case"
    ${ser_name} =  Set Variable      Amazon Elastic Compute Cloud
    Utilization.Perform action on Utilization   ${ser_name}


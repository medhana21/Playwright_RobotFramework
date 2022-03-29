*** Settings ***
Documentation           This is a Coverage test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Coverage File Test Case
    Log  "This is coverage test case"
    ${platform} =  Set Variable      Linux
    Coverage.Perform action on Coverage   ${platform}


*** Settings ***
Documentation           This is a Resource test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
Resources File Test Case
    Log  "This is resource test case"
    ${res} =  set variable        RDS
    Resources.Perform action on Resource   ${res}


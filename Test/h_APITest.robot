*** Settings ***
Documentation           This is a API test file with Robot Framework
Resource                ../Library/Helper/CommonHelper.robot
Resource                ../Library/Helper/PageHelper.robot

Suite Setup             Launch Browser Engine
Suite Teardown          Quit Opened Browser

Test Setup              Open Cloudwiz Application
Test Teardown           Close Cloudwiz Application


*** Test Cases ***
API File Test Case
    Log  "This is API test case"
    API.Perform action on API


*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  matti
    Set Password  matti12345
    Set Password Confirmation  matti12345
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  matti12345
    Set Password Confirmation  matti12345
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  ma
    Set Password Confirmation  ma
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  matti12345
    Set Password Confirmation  matti123456
    Submit Credentials
    Register Should Fail With Message  Password and confirmation do not match

Login After Successful Registration
    Set Username  matti
    Set Password  matti12345
    Set Password Confirmation  matti12345
    Submit Credentials
    Go To Login Page
    Set Username  matti
    Set Password  matti12345
    Submit LoginCredentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ma
    Set Password  matti12345
    Set Password Confirmation  matti12345
    Submit Credentials
    Go To Login Page
    Set Username  ma
    Set Password  matti12345
    Submit LoginCredentials
    Login Should Fail With Message  Invalid username or password
    

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit LoginCredentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
At start there are no todos
    Go To  ${HOME_URL}
    Title Should Be  Todo app
    Page Should Contain  things still unfinished: 0

After adding a todo, there is one
    Go To  ${HOME_URL}
    Click Link  Create new todo
    Input Text  content  Buy milk
    Click Button  Create
    Page Should Contain  things still unfinished: 1
    Page Should Contain  Buy milk

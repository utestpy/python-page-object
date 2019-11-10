#!/bin/bash


box() {
    echo "----------------------------------"
    echo "----- Running $1 tests -----------"
    echo "----------------------------------"
}


helper() {
    echo "Tool allows to simplify run of automated tests for blog project."
    echo ""
    echo "Available actions:"
    echo -e " - smoke\t\t run automated smoke tests"
    echo -e " - unittest\t\t run automated unittest tests"
    echo -e " - all\t\t\t run all automated tests"
    echo -e " - help\t\t\t display help"
    echo ""
    echo -e "Note:\t\t help will be provided in case of no input parameters"
}


raise-error-message() {
    echo "Invalid parameter <$1> is provided!"
    echo "Please use <smoke> or <unittest> key as a flag. For more info please use <help> flag"
    exit 1
}


clear-trash(){
    local trash='.pytest_cache'
    [[ -d "$trash" ]] && echo "removing ${trash} testing trash" && rm -rf ${trash} && echo "environment is cleared"
}


function unittests {
    pytest -v -m unittest tests/
}


function smoke {
    pytest -v -m smoke tests/
}


function all {
    pytest -v tests/
}


run-tests() {
    local arg=$1
    if [[ ${arg} == "smoke" ]] || [[ ${arg} == "unittest" ]];
        then box "${arg}" && pytest -m "${arg}"; clear-trash
    elif [[ ${arg} == "all" ]]
        then box "${arg}" && pytest; clear-trash
    elif [[ $# -eq 0 ]] || [[ ${arg} == "--help" ]] || [[ ${arg} == "-h" ]]
        then helper
    else raise-error-message "${arg}"
    fi
}

run-tests "$1"

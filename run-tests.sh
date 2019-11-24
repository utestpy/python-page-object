#!/bin/bash

FAILED_OUT="\033[0;31m"
YELLOW_OUT="\033[1;33m"
NONE_OUT="\033[0m"


function box() {
    echo "----------------------------------"
    echo "----- Running $1 tests -----------"
    echo "----------------------------------"
}


function helper {
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


function raise-error-message {
    echo -e "Invalid ${FAILED_OUT}$1${NONE_OUT} parameter is provided!"
    echo -e "Please use ${YELLOW_OUT}smoke${NONE_OUT} or ${YELLOW_OUT}unittest${NONE_OUT} key as a flag For more info please use ${YELLOW_OUT}help${NONE_OUT} flag."
    exit 1
}


function clear-trash {
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


function run-tests {
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

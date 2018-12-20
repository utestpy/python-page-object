#!/bin/bash

clear_trash(){
    local trash='.pytest_cache'
    [ -d "$trash" ] && echo "removing ${trash} testing trash" && rm -rf ${trash} && echo "environment is cleared"
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


function run_tests {
    local input="$1"
    [[ "${input}" == "all" ]] && all
    [[ "${input}" == "unittests" ]] && unittests
    [[ "${input}" == "smoke" ]] && smoke
    [[ $# == 0 ]] && echo 'Please use either "unittests", "smoke" or "all" parameters to run tests!'
    clear_trash

}

run_tests $1

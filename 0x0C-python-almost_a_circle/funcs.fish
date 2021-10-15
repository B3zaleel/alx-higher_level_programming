#!/usr/bin/fish

# E.g.; run_u_test base
#   => python3 -m unittest tests/test_models/test_base.py
# E.g.; run_u_test
#   => python3 -m unittest discover tests
function run_u_test
    if test (count $argv) -eq 1
        python3 -m unittest tests/test_models/test_$argv[1].py
    else
        python3 -m unittest discover tests
    end
end

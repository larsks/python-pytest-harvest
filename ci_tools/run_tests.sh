#!/usr/bin/env bash

cleanup() {
    rv=$?
    # on exit code 1 this is normal (some tests failed), do not stop the build
    if [ "$rv" = "1" ]; then
        exit 0
    else
        exit $rv
    fi
}

trap "cleanup" INT TERM EXIT

# First the raw
echo -e "\n\n****** Running tests : 1/2 RAW******\n\n"
pytest --cov-report term-missing --cov=./pytest_harvest -v pytest_harvest/tests_raw/

# Then the meta (appended)
echo -e "\n\n****** Running tests : 2/2 META******\n\n"
pytest --junitxml=reports/junit/junit.xml --html=reports/junit/report.html --cov-report term-missing --cov=./pytest_harvest --cov-append -v pytest_harvest/tests/
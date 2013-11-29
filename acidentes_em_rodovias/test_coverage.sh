#!/bin/bash
find . -type f -name "*.pyc" -exec rm -rfv '{}' \;
coverage erase
coverage run --source='app' manage.py test app
coverage report -m
coverage html -d ../../coverage


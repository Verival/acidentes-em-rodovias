#!/bin/bash
coverage erase
coverage run --source='.' manage.py test app
coverage report -m


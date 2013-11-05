#!/bin/bash
coverage erase
coverage run --source='app' manage.py test app
coverage report -m


#!/bin/bash
echo -n "Removing *.pyc ------------------------------------------ "
find . -type f -name "*.pyc" -exec rm -rf '{}' \;
echo "Done"
echo -n "Initing server ------------------------------------------"
#gnome-terminal -e python manage.py runserver &
echo "Done"
coverage erase
coverage run --source='app' manage.py test app
coverage report -m
coverage html -d ../../coverage


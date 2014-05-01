#!/bin/bash
echo -n "Removing *.pyc ------------------------------------------ "
find . -type f -name "*.pyc" -exec rm -rf "{}" \;
echo "Done"
echo -n "Initing server ------------------------------------------ "
python manage.py runserver 8000 &> /dev/null  &
echo "Done"
windmill firefox http://127.0.0.1:8000/acidentes_rodovias/ test=app/tests/tests_interface/tests_windmill &> /dev/null &
coverage erase
coverage run --source='app' manage.py test app
coverage report -m
coverage html -d ../../coverage
echo -n "Killing everything -------------------------------------- "
killall -9 coverage python test_coverage.sh -q
echo "Killed"
sleep 15
echo -n "Killing all --------------------------------------- "
kill $windmill-pid
killall -9 python windmill test_interface.sh -q
echo "Done"

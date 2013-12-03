#!/bin/bash
echo -n "Removing *.pyc ------------------------------------------ "
find . -type f -name "*.pyc" -exec rm -rf "{}" \;
echo "Done"
echo -n "Initing server ------------------------------------------ "
python manage.py runserver 8080 &> /dev/null  &
echo "Done"
coverage erase
coverage run --source='.' manage.py test app --with-xunit --xunit-file=app/tests/test-reports/nosetests.xml
coverage xml -o app/tests/test-reports/coverage.xml
echo -n "Killing dev server -------------------------------------- "
killall -9 coverage python test_coverage.sh -q
echo "Killed"
/opt/sonar-runner-2.3/bin/sonar-runner

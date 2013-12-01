#!/bin/bash
coverage erase
coverage run --source='.' manage.py test app --with-xunit --xunit-file=app/tests/test-reports/nosetests.xml
coverage xml -o app/tests/test-reports/coverage.xml
/opt/sonar-runner-2.3/bin/sonar-runner

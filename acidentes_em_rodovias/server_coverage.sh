#!/bin/bash
coverage erase
coverage run --source='.' manage.py test app
coverage xml -i -o app/tests/test-reports/coverage.xml
/opt/sonar-runner-2.3/bin/sonar-runner

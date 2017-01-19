echo on

start cmd /k "echo "***selenium webdriver window***" & start http://localhost:4444/wd/hub/static/resource/hub.html & webdriver-manager start"
::opens selenium webdriver for automated testing

start cmd /k "echo "***protractor window***" & npm run-script protractor"
::opens selenium webdriver for automated testing
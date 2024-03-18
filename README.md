# UI_testing_selenium

Selenium UI testing based on Chrome browser.
Sample test cases written in Python language.

## Used site
https://www.saucedemo.com/


## Used libraries

* PyTest - for running test cases
* PyTest-Html - for reporting
* PyTest-xdist - for running test cases on multiple workers
* Selenium - test platform

##Tips
To run test cases use -n parameter like **-n=4** for 4 workers
To run test reporting use -html paramter like **-html=reports/report.html** so html report file will be written in reports folder under the name "report"
To run test cases under specific marker use -m parameter like **-m login** so only login marked test cases will be run

Example:
5 workers, report in inventory_page_report.html and only inventory marked test cases
pytest -m inventory --html=reports/inventory_page_report.html -n=5

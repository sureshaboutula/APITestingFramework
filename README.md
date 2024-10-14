# Python API Automation Framework
''' Hybrid custom Framework to Test the REST APIs using the Pytest, Python, and allure Report '''

### Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, Pytest HTML
- Test Data - CSV, Excel, JSON, Faker
- Advance API TestCase - jsonschema
- Parallel Execution - x Distribute (xdist)

### How to install packages
''' pip install requests pytest pytest-html faker allure-pytest jsonschema '''
### How to run Testcases parallel
'pip install pytest-xdist'

### How to add the .gitignore File?

Copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm+all

### How to run the Basic Test with Allure Report
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s

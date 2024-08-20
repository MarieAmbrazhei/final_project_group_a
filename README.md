### final_project_group_a

## About

---
This project is an automated testing framework built to test the application
"https://thinking-tester-contact-list.herokuapp.com/"
It uses tools such as Pytest for test execution, Docker for containerization, and Jenkins for
continuous integration.  
Made by Yury Buzinau and Marie Ambrazhei.

## Project structure

---

```
/final_project_group_a
├── .github/
│   └── workflows/
│       └── ... (YAML files for CI/CD configurations)
├── allure_reports/            # Test reports generated after test execution
├── test_project/
│   ├── base_cls/
│   │   └── validate_response.py  # Manages HTTP responses, logs details, validates JSON data, asserts status codes
│   ├── pages/                 # Page objects and other source files
│   ├── pydentic_schemas/      # Pydantic models
│   ├── tests/
│   │   ├── api/               # API tests
│   │   └── ui/                # UI tests
│   ├── urls/                  # Endpoints and routes for API requests
│   └── utils/
│       ├── api/               # Methods
│       └── constants/         # Constants and error messages
├── venv/                      # Virtual environment
├── .gitignore                 # Files and directories ignored by Git
├── pytest.ini                 # Pytest configuration file
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

---

## Usage

---

### How to install

1. Clone the Repository:
    + `git clone <URL>`
    + cd final_project_group_a
2. Create virtual environment, activate it:
    + `pip install virtualenv`
    + `cd ~/projects/final_project_group_a`
    + `virtualenv venv`
    + `source venv/bin/activate`
3. Install dependencies
    + `pip install -r requirements.txt`

### How to run tests

1. To execute ALL tests w/ DEBUG log level
    + `pytest . --log-level=DEBUG`
2. To Execute All Tests:
    + `pytest .`
3. To Execute API Tests:
    + `pytest . -m api`
4. To execute UI test:
    + `pytest . -m ui`
5. To Execute Fast UI Tests (takes < 20 seconds):
    + `pytest . -m fast_ui`
6. To Execute Slow UI Tests (takes > 20 seconds):
    + `pytest . -m slow_ui`
7. To Execute Smoke UI Tests (critical tests):
    + `pytest . -m smoke_ui`

### Available markers:

- `api`: Marks tests related to API functionality.
- `ui`: Marks tests for user interface components.
- `fast_ui`: Marks tests that are fast (take < 20 seconds).
- `slow_ui`: Marks tests that are slow (take > 20 seconds).
- `smoke_ui`: Marks critical tests for user interface components.

### Additional Commands

1. To Generate Allure Reports:
    + `pytest --alluredir=allure_reports`
2. To Run Tests in Parallel:
    + `pytest -n auto`
3. To Generate Allure Reports and Run Tests in Parallel:
    + `pytest --alluredir=allure_reports -n auto`
4. To Serve Allure Reports:
    + `allure serve allure_reports`

### Additional arguments

```shell
Options:

  --browser=<browser>          To run UI tests on specific browser: chrome\firefox
  --headless                   To run browser in headless mode
```

### Logging with Loguru.

# Install Loguru:

- Install Loguru using pip:
  `pip install loguru`

## Using the Logger:

Import Loguru and start logging with just a few lines of code:
`from loguru import logger`
`logger.success(f"Add User. Status code: {act_code} ")`

# Structured logging as needed. Loguru helps you track and manage logging efficiently:

`logger.info(f"Delete User")`
`logger.success(f"Delete User. Status code: {act_code} ")`
`logger.warning(f"Error while executing the request: {str(e)}")`

### Data Generation.

To create realistic and diverse test data, we use the Faker library.
Faker generates various types of random data needed for testing.

## Install Faker:

`pip install faker`

## Import Faker:

`  from faker import Faker`

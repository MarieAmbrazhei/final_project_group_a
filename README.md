### project_group_a

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
├── ci/                        # CI/CD related files
│   ├── Jenkinsfile_api        # Jenkinsfile for API pipeline
│   ├── Jenkinsfile_ui         # Jenkinsfile for UI pipeline
│   └── Dockerfile             # Dockerfile for building Jenkins image with Pyt
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

1. To Execute All Tests:
    + `pytest .`
2. To Execute API Tests:
    + `pytest . -m api`
3. To execute UI test:
    + `pytest . -m ui`
4. To Execute Fast UI Tests (takes < 20 seconds):
    + `pytest . -m fast_ui`
5. To Execute Slow UI Tests (takes > 20 seconds):
    + `pytest . -m slow_ui`
6. To Execute Smoke UI Tests (critical tests):
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

### Jenkins Setup with Python in Docker

This guide walks you through the process of setting up Jenkins in a Docker container, installing
Python and Allure, and configuring the environment for running your first Jenkins job.

### Prerequisites

- **Docker** installed on your machine.
- **GitHub Personal Access Token** (for accessing private repositories).

### Step 1: Pull Jenkins Docker Image

Pull the latest Jenkins image from Docker Hub:

```bash
docker pull jenkins/jenkins
```

### Step 2: Build the Docker Image

```
docker build -t my-project-image .
```

### Step 3: Run Jenkins Container

```
docker run -d -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins
```

### Step 4: Retrieve Jenkins Initial Admin Password

To access Jenkins for the first time, you'll need the initial admin password.
Run the following command:

```
docker exec -it <container-id> cat /var/jenkins_home/secrets/initialAdminPassword
```

Replace <container-id> with your actual container ID. The command will return a password
similar to this:

```
4d4df420dd3c44939b1769d74fb21f98
```

### Step 5: Access Jenkins

Open your browser and go to http://localhost:8080. Use the following credentials to log in:

Username: admin
Password: <retrieved-password>
Replace <retrieved-password> with the password obtained in Step 4.

### Step 6: Setup First Job - Freestyle

- In Jenkins, create a new job of type "Freestyle project."
- Under Source Code Management, select GIT.
- Copy your repository URL (HTTPS) and paste it in the repository URL field.
- To set up credentials, follow these steps:
    - Click on Add next to the Credentials field.
    - Domain: Leave as Global or choose an appropriate domain.
    - Kind: Select Username with password.
    - Scope: Choose Global (Jenkins, nodes, items, all child items, etc.).
    - Username: Enter your GitHub username.
    - Password: Enter the GitHub Personal Access Token.
    - ID: (Optional) Provide an identifier for these credentials.
    - Description: (Optional) Provide a description for these credentials.
- Go to Branches to build and specify your Git branch.
- In the Build section, select Add build step -> Execute shell and provide
  the necessary shell commands.

### Step 7: Configure Jenkins Environment

Connect to your running Jenkins container and install the necessary tools:

```
docker exec -u root -it <container-id> /bin/bash
```

Inside the container, run the following commands:
Update package lists:

```
apt-get update
```

Install Python 3 and pip:

```
apt-get install python3
apt-get install python3-pip -y
python3 --version
pip3 --version
```
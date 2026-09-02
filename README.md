# CRM UI Test Automation

Python and Playwright test automation framework for validating the CRM web application's authentication and dashboard experience. The project uses Pytest for test execution, Page Object Model classes for maintainable UI interactions, and Allure for test reporting and failure artifacts.

## Project Overview

This repository contains end-to-end UI tests for the CRM dashboard. Tests run against a configured CRM environment and authenticate with an administrator account before exercising dashboard functionality.

The current coverage includes:

- Successful login and dashboard visibility
- Left navigation menu visibility
- Dashboard widget visibility
- Active dashboard menu state
- Header icon visibility
- User search and search-result navigation
- Invoice, lead, project, and task progress-bar values

The framework creates Playwright screenshots, videos, traces, and application logs to help investigate failures. These artifacts are attached to Allure results where supported by the test hooks.

## Tech Stack

| Technology | Purpose |
| --- | --- |
| Python 3.11 | Test automation language and CI runtime |
| Playwright | Browser automation and Chromium execution |
| Pytest | Test runner, fixtures, parametrization, and markers |
| `pytest-playwright` | Pytest integration for Playwright |
| Allure Report | Test results, steps, metadata, and failure evidence |
| GitHub Actions | Continuous integration and scheduled test execution |
| `python-dotenv` | Loading local environment variables from `.env` |
| `pytest-xdist` | Parallel test execution support |
| Faker / `jsonschema` / PyYAML | Test-data and utility dependencies available to the framework |

## Project Structure

```text
.
├── .env_example                 # Environment-variable template
├── .github/
│   └── workflows/
│       └── playwright.yml       # GitHub Actions test and Allure pipeline
├── config/
│   └── environments.json        # Example environment definitions
├── data/
│   └── dashboard_data.json      # Dashboard test data
├── page/
│   ├── base_page.py             # Shared Playwright interaction helpers
│   ├── login_page.py            # Login Page Object Model
│   └── dashboard_page.py        # Dashboard locators, actions, and checks
├── tests/
│   ├── test_verify_dashboard_display.py
│   └── test_verify_db_main_element_display.py
├── utils/
│   ├── allure_helper.py          # Allure attachments and Playwright tracing
│   ├── load_json.py              # JSON-loading helper
│   └── logger.py                 # File and console logging setup
├── conftest.py                  # Browser, authentication, page, and hooks
├── pytest.ini                   # Pytest defaults
├── requirements.txt              # Python dependencies
├── allure-results/              # Generated raw Allure results (ignored)
├── allure-report/               # Generated HTML report (ignored)
├── screenshots/                 # Failure screenshots (ignored)
├── videos/                      # Recorded browser videos (ignored)
├── traces/                      # Playwright trace ZIP files (ignored)
└── logs/                        # Automation logs (ignored)
```

The generated artifact directories may not exist until the test suite runs. Authentication state is stored under `auth/` when used and is intentionally excluded from version control.

## Local Setup & Configuration

### Prerequisites

- Python 3.11 or a compatible supported Python version
- Node.js/npm, required by the local Allure CLI installation
- Java, required by the Allure CLI
- Git

### 1. Create and activate a virtual environment

From the repository root on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Python dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install --with-deps
```

The current browser fixture launches headless Chromium.

### 4. Configure environment variables

Copy the template and replace its placeholder values with credentials for a non-production test account:

```powershell
Copy-Item .env_example .env
```

The test runtime currently reads these variables from `.env`:

| Variable | Required by current tests | Description |
| --- | --- | --- |
| `BASE_URL` | Yes | CRM URL used for navigation and login |
| `ADMIN_EMAIL` | Yes | Administrator email used during session setup |
| `ADMIN_PASSWORD` | Yes | Administrator password used during session setup |

The template also contains `DEV_BASE_URL`, `STAGING_BASE_URL`, `PROD_BASE_URL`, `STAGING_USERNAME`, `STAGING_PASSWORD`, `ADMIN_USERNAME`, `USER_FULL_NAME`, `USER_PASSWORD`, and `USER_USERNAME`. These are available for future or extended scenarios, but the current `conftest.py` login flow uses `BASE_URL`, `ADMIN_EMAIL`, and `ADMIN_PASSWORD` only.

Do not commit `.env` or real credentials. The repository ignore rules exclude local environment files and sensitive authentication data.

> **Configuration note:** `.env_example` defines environment-specific URL names, while the executable test code expects `BASE_URL`. Set `BASE_URL` explicitly in `.env`. The CI workflow currently maps the GitHub Repository/Environment **Variable** named `BASE_URL` to that runtime variable.

## Running Tests Locally

Run the complete suite and write raw Allure results:

```bash
pytest --alluredir=allure-results
```

Run with more verbose output and shorter failure tracebacks, matching CI:

```bash
pytest --alluredir=allure-results -v --tb=short
```

Run a subset using the current Pytest markers:

```bash
pytest -m smoke --alluredir=allure-results
pytest -m regression --alluredir=allure-results
pytest -m "ui and functional" --alluredir=allure-results
```

The test hooks create failure screenshots, video recordings, Playwright traces, and `logs/automation.log`. Test steps and metadata are added to Allure through `allure-pytest`.

### View the Allure report locally

Install the Allure command-line tool if it is not already available, then serve the results:

```bash
allure serve allure-results
```

The command generates a temporary report and opens it in a browser. To generate a reusable report directory instead:

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## CI/CD Pipeline: GitHub Actions

The workflow is defined in `.github/workflows/playwright.yml` and runs on `ubuntu-latest` with Python 3.11. It installs dependencies and Playwright browsers, executes the suite, uploads raw Allure results, generates an HTML report, and publishes the report to the `gh-pages` branch.

### Automatic and manual triggers

- **Pull request:** when a PR targets `master`
- **Push:** when code is pushed to `master`
- **Version tag:** when a tag matching `v*` is pushed
- **Schedule:** `0 0 * * 2,4,6` UTC, which is 07:00 Vietnam time on Tuesday, Thursday, and Saturday
- **Manual:** via GitHub Actions `workflow_dispatch`
- **Release:** when a release is published

### Required GitHub configuration

The workflow uses the `developer` GitHub Environment. Configure the following values in **Repository settings > Environments > developer** (or in the repository-level settings when appropriate):

| Name | Type | Required | Used by |
| --- | --- | --- | --- |
| `BASE_URL` | Variable | Yes | Target CRM URL passed to Pytest |
| `ADMIN_EMAIL` | Secret | Yes | Administrator login email |
| `ADMIN_PASSWORD` | Secret | Yes | Administrator login password |
| `GITHUB_TOKEN` | Automatic secret | Yes | Publishing the report to `gh-pages` |

For repository conventions that use `REPO_BASE_URL`, treat it as the logical name for the target URL and either:

1. copy its value to the workflow Environment Variable `BASE_URL`, or
2. update `playwright.yml` and the test configuration consistently to use `REPO_BASE_URL`.

The checked-in workflow currently references `vars.BASE_URL`, not `vars.REPO_BASE_URL`. The current workflow also authenticates only with admin credentials. User credentials from `.env_example` should be added as GitHub Environment Secrets only when user-role tests are implemented, for example `USER_USERNAME`, `USER_PASSWORD`, or `USER_FULL_NAME` as required by those tests. Never place passwords in GitHub Variables or source files.

### Pipeline stages

1. Check out the repository.
2. Set up Python 3.11 and cache pip packages.
3. Install Python dependencies and Playwright browser dependencies.
4. Run Pytest and upload `allure-results` as an artifact.
5. Restore previous Allure history from `gh-pages` when available.
6. Generate and upload the HTML Allure report.
7. Publish the report to the `gh-pages` branch using `GITHUB_TOKEN`.

### View the published Allure report

Enable GitHub Pages for the repository and select the `gh-pages` branch as the publishing source. After a successful workflow run, open:

```text
https://<github-owner>.github.io/<repository-name>/
```

Replace `<github-owner>` and `<repository-name>` with the repository's actual values. The report may take a short time to become available after the workflow finishes. The workflow also retains `allure-report` as a downloadable Actions artifact.

## Maintenance Notes

- Keep selectors and page actions inside the relevant Page Object class.
- Keep secrets in local `.env` files or GitHub Secrets; do not commit authentication state.
- Update expected dashboard values in the test parametrization when the test environment's legitimate data changes.
- Preserve Allure history on `gh-pages` so trend information is retained between pipeline runs.
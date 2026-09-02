# Customer Tester - Dashboard Automation Test Suite

## Project Overview

A comprehensive automated testing framework for dashboard functionality using Playwright and pytest. This project verifies core dashboard elements, user interactions, and data visualization components.

## Project Structure

```
Customer_tester/
├── tests/
│   ├── test_verify_db_main_element_display.py    # Dashboard element tests
│   └── README.md                                  # Test suite documentation
├── page/
│   ├── base_page.py                              # Base page object class
│   ├── login_page.py                             # Login page object
│   ├── dashboard_page.py                         # Dashboard page object
│   └── __pycache__/
├── data/
│   ├── login_data.json                           # Login credentials
│   └── [other test data files]
├── config/
│   ├── environments.json                         # Environment configuration
│   └── [other config files]
├── auth/
│   └── auth.json                                 # Stored authentication state
├── utils/
│   ├── logger.py                                 # Logging utility
│   ├── allure_helper.py                          # Allure reporting helper
│   ├── load_json.py                              # JSON file loader
│   └── [other utilities]
├── conftest.py                                   # Pytest fixtures and configuration
├── pytest.ini                                    # Pytest configuration
├── requirements.txt                              # Python dependencies
├── allure-report/                                # Allure HTML reports
├── allure-results/                               # Allure result files
├── screenshots/                                  # Test screenshots
├── videos/                                       # Browser recordings
├── traces/                                       # Playwright traces
├── logs/                                         # Test execution logs
└── README.md                                     # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- Playwright browsers installed
- Virtual environment (recommended)

### Installation

1. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

2. **Activate virtual environment**
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_verify_db_main_element_display.py -v

# Run with markers
pytest tests/ -m smoke -v
pytest tests/ -m regression -v

# Run with Allure reporting
pytest tests/ -v --alluredir=allure-results
```

## Test Suites

### Dashboard Element Display Tests
Located in `tests/test_verify_db_main_element_display.py`

**Classes:**
- `TestDashboardDisplay` - Display element verification
- `TestSearchFunctionality` - Search feature tests
- `TestProgressBars` - Progress bar validation

See [tests/README.md](tests/README.md) for detailed documentation.

## Framework Components

### Page Objects (`page/`)
Page object model implementation for maintainability:
- **BasePage** - Common methods for all page objects
- **LoginPage** - Login functionality
- **DashboardPage** - Dashboard elements and interactions

### Utilities (`utils/`)
Helper functions for testing:
- **logger** - Structured logging
- **allure_helper** - Allure report integration
- **load_json** - Configuration and test data loading

### Configuration
- **conftest.py** - Pytest fixtures (browser, context, page, dashboard_page)
- **pytest.ini** - Pytest settings
- **requirements.txt** - Python dependencies
- **data/login_data.json** - Test credentials
- **config/environments.json** - Environment URLs

## Key Features

### Authentication Management
- Automatic login on first run
- Session persistence with cookie storage
- Automatic session validation

### Test Organization
- Tests grouped in classes by functionality
- Clear naming conventions
- Comprehensive documentation

### Reporting
- Pytest verbose output
- Allure detailed reports with steps
- Browser video recordings
- Playwright traces for debugging
- Test screenshots on failure

### Best Practices
- Page Object Model pattern
- Fixture-based test data
- Parameterized testing
- Pytest markers for test selection
- Type hints for better code clarity

## Running Different Test Types

### Smoke Tests
Quick validation of critical functionality:
```bash
pytest tests/ -m smoke -v
```

### Regression Tests
Full test suite:
```bash
pytest tests/ -m regression -v
```

### UI Tests
All visual/UI related tests:
```bash
pytest tests/ -m ui -v
```

### Functional Tests
Feature-specific tests:
```bash
pytest tests/ -m functional -v
```

## Generating Reports

### Allure Reports
```bash
# Run tests with Allure reporting
pytest tests/ -v --alluredir=allure-results

# Generate and serve Allure report
allure serve allure-results
```

### HTML Report
```bash
pytest tests/ -v --html=report.html
```

## Configuration Files

### login_data.json
```json
[
  {
    "url": "https://example.com",
    "username": "your_username",
    "password": "your_password"
  }
]
```

### environments.json
```json
{
  "base_url": "https://example.com",
  "timeout": 30000
}
```

## Troubleshooting

### Import Errors
```bash
# Ensure virtual environment is activated
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Playwright Issues
```bash
# Reinstall Playwright
pip install --force-reinstall playwright
playwright install
```

### Authentication Failures
- Delete `auth/auth.json` to force re-login
- Verify credentials in `data/login_data.json`
- Check if website changed login process

### Flaky Tests
- Check network stability
- Increase timeouts if necessary
- Review element locators for UI changes

## Development Workflow

### Adding New Tests
1. Create page object methods in `page/dashboard_page.py`
2. Add test methods to appropriate test class
3. Use fixtures from `conftest.py`
4. Add appropriate pytest markers
5. Include allure steps for reporting

### Updating Test Data
1. Modify fixtures in `conftest.py`
2. Or update JSON files in `data/` or `config/`
3. Run tests to verify changes

### Debugging Tests
```bash
# Run with verbose output
pytest tests/test_file.py -v -s

# Run specific test with debugging
pytest tests/test_file.py::TestClass::test_method -v -s --pdb
```

## Dependencies

See `requirements.txt` for all dependencies:
- **pytest** - Test framework
- **playwright** - Browser automation
- **allure-pytest** - Allure reporting
- **pytest-html** - HTML reporting

## CI/CD Integration

These tests can be integrated into CI/CD pipelines:
```bash
# Example GitHub Actions, Jenkins, etc.
pytest tests/ -v --alluredir=allure-results --html=report.html
```

## Best Practices

1. **Always use fixtures** for test setup/teardown
2. **Group related tests** in test classes
3. **Use page objects** for element interactions
4. **Parametrize** similar tests
5. **Add meaningful assertions** with clear messages
6. **Include allure steps** for better reporting
7. **Use pytest markers** for test categorization

## Performance

- Average test execution time: ~30-60 seconds per test
- Parallel execution supported with pytest-xdist
- Video recording and tracing can be disabled for faster execution

## Documentation

- [Test Suite Documentation](tests/README.md)
- [Dashboard Page Object](page/dashboard_page.py)
- [Base Page Object](page/base_page.py)

## Contributing

1. Follow the established test structure
2. Use page object model
3. Add comprehensive docstrings
4. Include pytest markers
5. Add allure decorations
6. Update README if adding new features

## License

[Your License Here]

## Contact

For questions or issues, please contact the test automation team.

## Changelog

### Version 1.0 (Current)
- Initial test suite for dashboard elements
- Search functionality tests
- Progress bar verification tests
- Allure and pytest marker integration
- Comprehensive documentation

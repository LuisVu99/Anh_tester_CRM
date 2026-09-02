import pytest
import allure

@allure.feature("Dashboard display")
@allure.story("Dashboard element")
@allure.title("Verify Dashboard page display successfully after login")
def test_verify_dashboard_display(login_page):
    with allure.step((f"Verify display: expected element in Dashboard display")):
        assert login_page.is_dashboard_visible(), \
            f"Dashboard is not displayed successfully"

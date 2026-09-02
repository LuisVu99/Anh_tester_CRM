
"""
Dashboard Main Element Display Tests

Tests to verify all main dashboard elements are properly displayed and functional.
Includes tests for menu, widgets, search, progress bars, and header icons.
"""

import pytest
import allure


@allure.feature("Dashboard Display")
@allure.story("Dashboard Elements")
class TestDashboardDisplay:
    """Tests for dashboard display elements"""

    @pytest.mark.smoke
    @pytest.mark.ui
    @allure.title("Verify left menu is visible")
    def test_verify_left_menu_display(self, dashboard_page):
        """Verify left menu is visible on dashboard"""
        with allure.step("Check left menu visibility"):
            dashboard_page.verify_left_menu_is_visible()

    @pytest.mark.regression
    @pytest.mark.ui
    @allure.title("Verify all widgets are displayed")
    def test_verify_all_widgets_displayed(self, dashboard_page):
        """Verify all dashboard widgets are displayed"""
        with allure.step("Verify all widgets visibility"):
            dashboard_page.verify_all_widgets_visible()

    @pytest.mark.smoke
    @pytest.mark.ui
    @allure.title("Verify dashboard menu is highlighted")
    def test_verify_dashboard_highlighted(self, dashboard_page):
        """Verify dashboard menu item is highlighted"""
        with allure.step("Check dashboard menu highlight"):
            dashboard_page.verify_dashboard_is_active()

    @pytest.mark.regression
    @pytest.mark.ui
    @allure.title("Verify all header icons are displayed")
    def test_verify_header_icon_display(self, dashboard_page):
        """Verify all header icons are displayed"""
        with allure.step("Check header icons visibility"):
            dashboard_page.verify_all_header_icons_visible()


@allure.feature("Dashboard Search")
@allure.story("Search Functionality")
class TestSearchFunctionality:
    """Tests for dashboard search functionality"""

    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("Verify search results match query")
    def test_verify_search_result(self, dashboard_page, search_test_data):
        """Verify search results match the search query
        
        Args:
            dashboard_page: Dashboard page object
            search_test_data: Fixture containing search username
        """
        search_username = search_test_data["username"]
        
        with allure.step(f"Search for user: {search_username}"):
            dashboard_page.search_by_username(search_username)
        
        with allure.step(f"Verify search results contain: {search_username}"):
            dashboard_page.get_search_result_text(0)

        with allure.step(f"Verify search results contain keyword: {search_username}"):
            dashboard_page.verify_search_results_contain_keyword(search_username)

        with allure.step(f"Click on search result {search_username}"):
            dashboard_page.click_first_search_result()


@allure.feature("Dashboard Progress Bars")
@allure.story("Progress Bar Verification")
class TestProgressBars:
    """Tests for dashboard progress bar elements"""

    @pytest.mark.parametrize("widget_type,method_type,expected_fraction,expected_percent", [
        pytest.param("invoice", "invoice", "3 / 6", "50.00", id="invoice_progress"),
        pytest.param("lead", "lead", "0 / 0", "0", id="lead_progress"),
        pytest.param("project", "project", "69 / 157", "43.95", id="project_progress"),
        pytest.param("task_not_finish", "task", "247 / 248", "99.60", id="task_progress")
    ])
    @pytest.mark.regression
    @pytest.mark.ui
    @allure.title("Verify {widget_type} progress bar values")
    def test_verify_progress_bar(self, dashboard_page, widget_type, method_type, expected_fraction, expected_percent):
        """Verify progress bar fraction and percentage match expected values
        
        Args:
            dashboard_page: Dashboard page object
            widget_type: Type of progress bar (invoice, lead, project, task_not_finish)
            expected_fraction: Expected fraction value (e.g., "3 / 6")
            expected_percent: Expected percentage value (e.g., "50.00")
        """
        # Get methods based on widget type
        fraction_method = getattr(dashboard_page, f"get_{method_type}_progress_fraction")
        percent_method = getattr(dashboard_page, f"get_{method_type}_progress_percent")

        with allure.step(f"Get {widget_type} progress bar fraction"):
            actual_fraction = fraction_method()
        
        with allure.step(f"Get {widget_type} progress bar percentage"):
            actual_percent = percent_method()

        with allure.step(f"Verify {widget_type} fraction: expected {expected_fraction}, got {actual_fraction}"):
            assert actual_fraction == expected_fraction, \
                f"{widget_type} fraction mismatch: expected {expected_fraction}, got {actual_fraction}"
        
        with allure.step(f"Verify {widget_type} percent: expected {expected_percent}, got {actual_percent}"):
            assert actual_percent == expected_percent, \
                f"{widget_type} percent mismatch: expected {expected_percent}, got {actual_percent}"

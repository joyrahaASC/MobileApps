import pytest
from libs.flows.windows.flow_container import FlowContainer


@pytest.mark.usefixtures("windows_test_setup")
class TestSuite02Feedback:
    """
    Test Suite 02: Feedback functionality verification
    """

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, windows_test_setup):
        """Setup fixture for test class"""
        cls = self.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.feedback = request.cls.fc.fd["feedback"]

    def test_feedback_flow(self):
        """
        Test Case: Verify feedback flow from profile to feedback options
        Steps:
        1. Verify profile icon is visible
        2. Click the profile button
        3. Verify feedback button is present
        4. Click the feedback button
        5. Verify title 'Why did you open the app today?' is displayed
        6. Verify options list is visible under the title
        """
        # Step 1: Verify profile icon is visible
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon should be visible"

        # Step 2: Click the profile button
        self.devicesMFE.click_profile_button()

        # Step 3: Verify feedback button is present
        assert self.feedback.verify_feedback_button_present(), "Feedback button should be present"

        # Step 4: Click the feedback button
        self.feedback.click_feedback_button()

        # Step 5: Verify title 'Why did you open the app today?' is displayed
        assert self.feedback.verify_feedback_title_displayed(), "Feedback title should be displayed"

        # Step 6: Verify options list is visible under the title
        assert self.feedback.verify_options_list_visible(), "Options list should be visible"

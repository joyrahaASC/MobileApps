import pytest
from libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


class TestSuite02Feedback:
    """
    Test Suite 02: Feedback functionality tests
    """

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, windows_test_setup):
        cls = self.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.feedback = request.cls.fc.fd["feedback"]
        cls.profilePanel = request.cls.fc.fd["profilePanel"]
        cls.flowContainer = request.cls.fc.fd["flowContainer"]

    def test_feedback_workflow(self):
        """
        Test feedback workflow with profile and feedback interactions
        """
        # Step 1: Verify why did you open the app today options list is present
        self.feedback.verify_why_did_you_open_app_today_list()

        # Step 2: Assert title is 'Why did you open the app today?'
        self.feedback.assert_why_did_you_open_app_today_title()

        # Step 3: Verify profile icon is visible
        self.profilePanel.verify_profile_icon_visible()

        # Step 4: Verify feedback button is present
        self.profilePanel.verify_feedback_button_present()

        # Step 5: Click feedback button
        self.profilePanel.click_feedback_button()

        # Step 6: Click profile button
        self.flowContainer.click_profile_button()

import pytest
from libs.flows.windows.flow_container import FlowContainer


class TestSuite02Feedback:
    """Test suite for feedback functionality"""

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, windows_test_setup):
        cls = self.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.feedback = request.cls.fc.fd["feedback"]

    def test_feedback_flow(self):
        """Test feedback flow from profile to feedback options"""
        # Verify profile icon is visible
        self.devicesMFE.verify_profile_icon_show_up()
        
        # Click the profile button
        self.devicesMFE.click_profile_button()
        
        # Verify feedback button is present
        self.feedback.verify_feedback_button_present()
        
        # Click the feedback button
        self.feedback.click_feedback_button()
        
        # Verify title 'Why did you open the app today?' is displayed
        self.feedback.verify_feedback_title_displayed()
        
        # Verify options list is visible under the title
        self.feedback.verify_options_list_visible()
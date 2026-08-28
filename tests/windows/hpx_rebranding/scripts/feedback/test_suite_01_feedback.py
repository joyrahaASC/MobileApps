import pytest
from libs.flows.windows.flow_container import FlowContainer


class TestFeedback:
    """
    Test suite for feedback functionality
    """

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, windows_test_setup):
        cls = self.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.profilePanel = request.cls.fc.fd["profilePanel"]
        cls.feedbackScreen = request.cls.fc.fd["feedbackScreen"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]

    def test_feedback_flow(self):
        """
        Test feedback flow with profile interaction and text validation
        """
        # Click profile button
        self.profilePanel.click_profile_button()
        
        # Verify feedback button is present
        self.profilePanel.verify_feedback_button_present()
        
        # Click feedback button
        self.profilePanel.click_feedback_button()
        
        # Verify edit feedback screen is displayed
        self.feedbackScreen.verify_feedback_screen_displayed()
        
        # Input tell your experience text
        self.feedbackScreen.input_experience_text()
        
        # Get tell your experience text value
        self.feedbackScreen.get_experience_text_value()
        
        # Assert tell your experience text is truncated to maximum characters
        self.feedbackScreen.verify_experience_text_max_length()
        
        # Verify profile icon is visible
        self.devicesMFE.verify_profile_icon_show_up()

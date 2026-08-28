import pytest
from libs.flows.windows.flow_container import FlowContainer


class TestFeedback:
    """Test suite for feedback functionality"""

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, windows_test_setup):
        cls = self.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.profilePanel = request.cls.fc.fd["profilePanel"]

    def test_feedback_flow(self):
        """Test feedback button visibility and interaction"""
        # Verify profile icon is visible
        self.devicesMFE.verify_profile_icon_show_up()
        
        # Click profile button
        self.profilePanel.click_profile_button()
        
        # Verify feedback button is present
        self.profilePanel.verify_feedback_button_present()
        
        # Click feedback button
        self.profilePanel.click_feedback_button()
        
        # Assert feedback button should be present
        self.profilePanel.assert_feedback_button_present()

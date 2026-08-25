import pytest
from libs.flows.windows.hpx_rebranding import HPXRebrandingFlow


class TestC84:
    """Test case C84: Verify feedback functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, windows_driver):
        """Setup fixture for test initialization"""
        self.driver = windows_driver
        self.hpx_rebranding_flow = HPXRebrandingFlow(self.driver)
        yield
        # Teardown logic if needed

    def test_feedback_flow(self):
        """Test feedback flow with profile icon, feedback button and text input"""
        
        # Step 1: Verify profile icon is visible
        self.hpx_rebranding_flow.verify_profile_icon_show_up()
        
        # Step 2: Click the profile button
        self.hpx_rebranding_flow.click_devicepage_avatar_btn()
        
        # Step 3: Verify feedback button is present
        self.hpx_rebranding_flow.verify_feedback_btn()
        
        # Step 4: Click the feedback button
        self.hpx_rebranding_flow.click_feedback_btn()
        
        # Step 5: Verify edit feedback screen is displayed
        self.hpx_rebranding_flow.verify_edit_feedback()
        
        # Step 6: Input tell your experience text
        self.hpx_rebranding_flow.input_tell_your_experience()
        
        # Step 7: Get tell your experience text value
        entered_text = self.hpx_rebranding_flow.get_entered_text()
        assert entered_text is not None, "Failed to retrieve entered text"

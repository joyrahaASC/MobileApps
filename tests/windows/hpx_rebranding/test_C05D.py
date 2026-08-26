import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_C05D(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.feedback = request.cls.fc.fd["feedback"]

    @pytest.mark.regression
    def test_01_verify_feedback_text_box_character_limit_C05D(self):
        """Verify the text box accepts a maximum of 2000 characters and truncates any additional input."""
        # Step 1: Ensure the profile icon is visible and click the profile button
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        self.profile.click_profile_button()
        
        # Step 2: Verify the feedback button is present and click it
        assert self.profile.verify_feedback_button(), "feedback button not present"
        self.profile.click_feedback_button()
        
        # Step 3: Verify the edit feedback screen opens
        assert self.feedback.verify_edit_feedback_screen(), "edit feedback screen not displayed"
        
        # Step 4: Input a text string longer than 2000 characters into the 'tell your experience' text box
        assert self.feedback.verify_tell_your_experience_textbox(), "tell your experience text box not visible"
        
        # Generate a string longer than 2000 characters
        long_text = "A" * 2500
        self.feedback.input_tell_your_experience_text(long_text)
        
        # Get the actual text value from the text box
        actual_text = self.feedback.get_tell_your_experience_text_value()
        
        # Assert the text is truncated to 2000 characters
        assert len(actual_text) == 2000, f"Text box did not truncate to 2000 characters. Actual length: {len(actual_text)}"
        assert actual_text == "A" * 2000, "Text box content does not match expected truncated value"

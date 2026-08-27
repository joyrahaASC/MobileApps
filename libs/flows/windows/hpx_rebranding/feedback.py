import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class Feedback(HPXRebrandingFlow):
    flow_name = "feedback"

    def verify_edit_feedback_screen_displayed(self):
        """
        Verify edit feedback screen is displayed.
        Wait for and verify that the edit feedback screen is displayed with all required elements
        (text input field, submit button, etc.). Return True if displayed correctly, False otherwise.
        """
        try:
            edit_feedback_element = self.driver.wait_for_object("edit_feedback", raise_e=False, timeout=10)
            submit_btn_element = self.driver.wait_for_object("send_feedback_submit_btn", raise_e=False, timeout=10)
            title_element = self.driver.wait_for_object("tell_your_experience_title", raise_e=False, timeout=10)
            
            if edit_feedback_element and submit_btn_element and title_element:
                return True
            else:
                return False
        except:
            return False

    def input_tell_your_experience_text(self, text):
        """
        Input tell your experience text.
        Wait for the 'tell your experience' text input field to be visible and interactable.
        Clear any existing text and input the provided text parameter.
        Should handle text that exceeds 2000 characters.
        """
        self.driver.wait_for_object("edit_feedback", timeout=10)
        edit_feedback_element = self.driver.wait_for_object("edit_feedback", timeout=10)
        self.driver.clear_text("edit_feedback")
        self.driver.send_keys("edit_feedback", text)

    def get_tell_your_experience_text_value(self):
        """
        Get tell your experience text value.
        Wait for the 'tell your experience' text input field and retrieve its current text value.
        Return the text as a string.
        """
        self.driver.wait_for_object("edit_feedback", timeout=10)
        text_value = self.driver.get_attribute("edit_feedback", "Value.Value", timeout=10)
        return text_value

    def assert_text_truncated_to_2000_chars(self, expected_text):
        """
        Assert tell your experience text is truncated to 2000 characters.
        Get the current text value from the 'tell your experience' field and assert that it is
        truncated to exactly 2000 characters if the input exceeded that limit.
        Compare with the expected truncated text. Should raise assertion error if validation fails.
        """
        actual_text = self.get_tell_your_experience_text_value()
        
        if len(expected_text) > 2000:
            expected_truncated = expected_text[:2000]
            assert len(actual_text) == 2000, f"Expected text length to be 2000, but got {len(actual_text)}"
            assert actual_text == expected_truncated, f"Expected text to be truncated to '{expected_truncated}', but got '{actual_text}'"
        else:
            assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
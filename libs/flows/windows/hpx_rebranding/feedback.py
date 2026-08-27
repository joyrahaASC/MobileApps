from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys


class Feedback(HPXRebrandingFlow):
    flow_name = "feedback"

    def verify_edit_feedback_screen_displayed(self):
        """
        Verify edit feedback screen is displayed.
        Wait for the edit feedback screen to be fully loaded and visible.
        Verify key elements like the feedback text input field, submit button, and screen title are present.
        Return True if screen is displayed correctly, False otherwise.
        """
        try:
            if self.driver.wait_for_object("hpx_feedback_page_title", raise_e=False, timeout=10) is False:
                return False
            if self.driver.wait_for_object("edit_feedback", raise_e=False, timeout=10) is False:
                return False
            self.driver.swipe("send_feedback_submit_btn")
            if self.driver.wait_for_object("send_feedback_submit_btn", raise_e=False, timeout=10) is False:
                return False
            if self.driver.wait_for_object("tell_your_experience_title", raise_e=False, timeout=10) is False:
                return False
            return True
        except Exception:
            return False

    def input_tell_your_experience_text(self, text):
        """
        Input tell your experience text.
        Wait for the 'tell your experience' text input field to be visible and interactable.
        Clear any existing text and input the provided text parameter.
        """
        self.driver.swipe("edit_feedback")
        self.driver.wait_for_object("edit_feedback", timeout=10)
        self.driver.click("edit_feedback", timeout=10)
        element = self.driver.wait_for_object("edit_feedback", timeout=10)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        self.driver.send_keys("edit_feedback", text)

    def get_tell_your_experience_text_value(self):
        """
        Get entered tell your experience text value.
        Wait for the 'tell your experience' text input field to be present and retrieve its current value/text content.
        Return the text as a string.
        """
        self.driver.swipe("edit_feedback")
        self.driver.wait_for_object("edit_feedback", timeout=10)
        text_value = self.driver.get_attribute("edit_feedback", "Value.Value")
        return text_value

    def assert_text_truncated_to_max_characters(self, expected_max_length):
        """
        Assert tell your experience text is truncated to characters.
        Get the current value of the 'tell your experience' text field and verify that its length
        does not exceed the expected maximum character limit.
        Raise an assertion error with descriptive message if validation fails.
        """
        self.driver.swipe("edit_feedback")
        self.driver.wait_for_object("edit_feedback", timeout=10)
        text_value = self.driver.get_attribute("edit_feedback", "Value.Value")
        actual_length = len(text_value)
        assert actual_length <= expected_max_length, f"Text length {actual_length} exceeds maximum allowed length {expected_max_length}"
        try:
            self.driver.wait_for_object("edit_feedback_char_count", raise_e=False, timeout=10)
            char_count_display = self.driver.get_attribute("edit_feedback_char_count", "Name")
        except Exception:
            pass

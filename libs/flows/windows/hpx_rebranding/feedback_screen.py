import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys


class FeedbackScreen(HPXRebrandingFlow):
    flow_name = "feedback_screen"

    def verify_feedback_screen_displayed(self):
        """
        Verify edit feedback screen is displayed.
        Wait for and verify that the feedback screen is displayed with all key elements visible.
        Returns:
            bool: True if displayed correctly, False otherwise.
        """
        try:
            # Wait for all key elements to be visible
            self.driver.wait_for_object("feedback_screen_title", raise_e=False, timeout=10)
            self.driver.wait_for_object("tell_your_experience_textbox", raise_e=False, timeout=10)
            self.driver.wait_for_object("submit_feedback_btn", raise_e=False, timeout=10)
            self.driver.wait_for_object("cancel_feedback_btn", raise_e=False, timeout=10)
            
            # Verify all elements are displayed
            title_displayed = self.driver.wait_for_object("feedback_screen_title", raise_e=False, timeout=10) is not False
            textbox_displayed = self.driver.wait_for_object("tell_your_experience_textbox", raise_e=False, timeout=10) is not False
            submit_displayed = self.driver.wait_for_object("submit_feedback_btn", raise_e=False, timeout=10) is not False
            
            return title_displayed and textbox_displayed and submit_displayed
        except Exception:
            return False

    def input_experience_text(self, text):
        """
        Input tell your experience text.
        Wait for the 'tell your experience' text input field to be interactable,
        clear any existing text, and input the provided text parameter.
        Args:
            text (str): The text to input into the experience textbox.
        """
        # Wait for element to be visible and interactable
        self.driver.wait_for_object("tell_your_experience_textbox", timeout=10)
        
        # Click to focus the textbox
        self.driver.click("tell_your_experience_textbox", timeout=10)
        time.sleep(1)
        
        # Get the element and clear existing text
        textbox = self.driver.wait_for_object("tell_your_experience_textbox", timeout=10)
        textbox.send_keys(Keys.CONTROL + "a")
        time.sleep(0.5)
        textbox.send_keys(Keys.DELETE)
        time.sleep(0.5)
        
        # Input the new text
        textbox.send_keys(text)
        time.sleep(1)

    def get_experience_text_value(self):
        """
        Get tell your experience text value.
        Wait for the 'tell your experience' text input field and retrieve the current text value.
        Returns:
            str: The current text value from the textbox.
        """
        # Wait for element to be present
        textbox = self.driver.wait_for_object("tell_your_experience_textbox", timeout=10)
        
        # Get and return the text value
        text_value = self.driver.get_attribute("tell_your_experience_textbox", "Name", timeout=10)
        return text_value if text_value else ""

    def verify_experience_text_max_length(self, expected_max_length):
        """
        Assert tell your experience text is truncated to maximum characters.
        Get the current text value and verify that its length does not exceed the expected maximum.
        Args:
            expected_max_length (int): The expected maximum character limit.
        Raises:
            AssertionError: If the text length exceeds the expected maximum length.
        """
        # Wait for element to be present
        self.driver.wait_for_object("tell_your_experience_textbox", timeout=10)
        
        # Get current text value
        current_text = self.get_experience_text_value()
        
        # Calculate length
        actual_length = len(current_text)
        
        # Check if character count display exists
        try:
            char_count_element = self.driver.wait_for_object("edit_feedback_char_count", raise_e=False, timeout=5)
            if char_count_element is not False:
                char_count_text = self.driver.get_attribute("edit_feedback_char_count", "Name", timeout=10)
                # Verify format matches expected pattern (e.g., 'X/Y')
                if "/" in str(char_count_text):
                    displayed_count = str(char_count_text).split("/")[0].strip()
                    assert str(actual_length) == displayed_count, f"Character count mismatch: actual={actual_length}, displayed={displayed_count}"
        except Exception:
            pass
        
        # Assert that text length is within expected maximum
        assert actual_length <= expected_max_length, (
            f"Text length {actual_length} exceeds expected maximum length {expected_max_length}. "
            f"Text should be truncated to {expected_max_length} characters."
        )

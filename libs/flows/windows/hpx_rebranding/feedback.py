from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys

class Feedback(HPXRebrandingFlow):
    flow_name = "feedback"

    def click_whats_your_feedback_related_to_options(self):
        self.driver.click("whats_your_feedback_related_to_options", timeout=10)

    def click_feedback_button(self):
        """
        Click the feedback button to navigate to the feedback screen.
        Waits for the feedback button element to be clickable, performs the click action,
        and verifies navigation to the feedback page.
        """
        self.driver.wait_for_object('menu_btn_from_feedback', timeout=10)
        self.driver.click('menu_btn_from_feedback', timeout=10)
        feedback_title = self.driver.wait_for_object('hpx_feedback_page_title', timeout=10)
        if not feedback_title:
            raise AssertionError("Failed to navigate to feedback page: 'hpx_feedback_page_title' not displayed")
        return True

    def verify_edit_feedback_screen_displayed(self):
        """
        Verify that the edit feedback screen is displayed.
        Checks for key elements that uniquely identify the feedback screen.
        Returns True if the screen is displayed, False otherwise.
        """
        try:
            feedback_title = self.driver.wait_for_object('hpx_feedback_page_title', timeout=10, raise_e=False)
            if not feedback_title:
                return False
            
            edit_feedback = self.driver.wait_for_object('edit_feedback', timeout=10, raise_e=False)
            if not edit_feedback:
                return False
            
            self.driver.swipe('send_feedback_submit_btn')
            submit_btn = self.driver.wait_for_object('send_feedback_submit_btn', timeout=10, raise_e=False)
            if not submit_btn:
                return False
            
            return True
        except Exception:
            return False

    def input_tell_your_experience_text(self, text: str):
        """
        Input text into the 'tell your experience' text field.
        
        Args:
            text (str): The text to be entered into the experience field.
        """
        self.driver.swipe('edit_feedback')
        self.driver.wait_for_object('edit_feedback', timeout=10)
        self.driver.click('edit_feedback', timeout=10)
        
        # Clear existing text
        edit_feedback_element = self.driver.get_element('edit_feedback')
        edit_feedback_element.clear()
        
        # Send the provided text
        self.driver.send_keys('edit_feedback', text)
        
        # Verify text was entered
        entered_text = self.driver.get_attribute('edit_feedback', 'Value.Value')
        if entered_text != text:
            raise AssertionError(f"Text verification failed. Expected: '{text}', but got: '{entered_text}'")
        
        return True

    def get_tell_your_experience_text_value(self):
        """
        Retrieve and return the current value of the 'tell your experience' text input field.
        
        Returns:
            str: The current text value in the field, or empty string if None.
        """
        self.driver.swipe('edit_feedback', direction='down')
        self.driver.wait_for_object('edit_feedback', timeout=10)
        text_value = self.driver.get_attribute('edit_feedback', 'Value.Value')
        return text_value if text_value is not None else ""

    def assert_tell_your_experience_text_truncated(self, expected_max_length: int):
        """
        Verify that the 'tell your experience' text has been truncated to the expected maximum length.
        
        Args:
            expected_max_length (int): The maximum allowed character length.
        
        Returns:
            bool: True if truncation is correctly applied.
        
        Raises:
            AssertionError: If validation fails with descriptive message.
        """
        self.driver.swipe('edit_feedback', direction='down')
        self.driver.wait_for_object('edit_feedback', timeout=10)
        
        # Get current text value
        current_text = self.driver.get_attribute('edit_feedback', 'Value.Value')
        if current_text is None:
            current_text = ""
        
        # Calculate actual character count
        actual_length = len(current_text)
        
        # Get character count display
        self.driver.wait_for_object('edit_feedback_char_count', timeout=10)
        char_count_display = self.driver.get_attribute('edit_feedback_char_count', 'Name', timeout=10)
        
        # Assert actual text length equals expected max length
        if actual_length != expected_max_length:
            raise AssertionError(
                f"Text truncation failed. Expected length: {expected_max_length}, but got: {actual_length}"
            )
        
        # Assert character count display shows expected format
        expected_display = f"{expected_max_length}/{expected_max_length}"
        if char_count_display != expected_display:
            raise AssertionError(
                f"Character count display mismatch. Expected: '{expected_display}', but got: '{char_count_display}'"
            )
        
        return True

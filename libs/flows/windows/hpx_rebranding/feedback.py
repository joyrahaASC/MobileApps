import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys

class Feedback(HPXRebrandingFlow):
    flow_name = "feedback"

    def verify_edit_feedback_screen_displayed(self):
        """
        Verify edit feedback screen is displayed.
        Wait for and verify that the edit feedback screen is visible.
        
        Returns:
            bool: True if the feedback page title is displayed
            
        Raises:
            Exception: If hpx_feedback_page_title is not found within timeout
        """
        return self.driver.wait_for_object("hpx_feedback_page_title")

    def verify_tell_your_experience_textbox_visible(self):
        """
        Verify tell your experience textbox is visible.
        Wait for and verify that the 'tell your experience' textbox element is visible on the feedback screen.
        
        Returns:
            bool: True if the edit_feedback textbox is displayed
            
        Raises:
            Exception: If edit_feedback is not found within timeout
        """
        return self.driver.wait_for_object("edit_feedback")

    def input_tell_your_experience_text(self, text):
        """
        Input tell your experience text.
        Locate the 'tell your experience' textbox and input the provided text string.
        
        Args:
            text (str): The text to input into the textbox
            
        Returns:
            None
        """
        self.driver.wait_for_object("edit_feedback")
        self.driver.send_keys("edit_feedback", text)

    def get_tell_your_experience_value(self):
        """
        Get the entered tell your experience value.
        Retrieve and return the current text value from the 'tell your experience' textbox.
        
        Returns:
            str: The current text in the textbox
        """
        self.driver.wait_for_object("edit_feedback")
        return self.driver.get_attribute("edit_feedback", "Name")

    def assert_tell_your_experience_text_truncated(self, expected_length):
        """
        Assert tell your experience text is truncated.
        Verify that the text in the 'tell your experience' textbox has been truncated to the expected maximum length.
        
        Args:
            expected_length (int): The maximum allowed character count
            
        Raises:
            AssertionError: If text length exceeds expected_length
        """
        self.driver.wait_for_object("edit_feedback")
        actual_text = self.driver.get_attribute("edit_feedback", "Name")
        actual_length = len(actual_text)
        assert actual_length == expected_length, f"Text length {actual_length} does not match expected length {expected_length}. Text was not properly truncated."
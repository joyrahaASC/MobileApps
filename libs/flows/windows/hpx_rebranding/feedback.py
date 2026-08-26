from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class FeedbackPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.locators = {
            "edit_feedback": None,
            "edit_feedback_char_count": None
        }

    def verify_edit_feedback_screen_displayed(self):
        """
        Verify edit feedback screen is displayed.
        Wait for the edit feedback screen to be fully loaded and displayed.
        Verify key elements of the feedback screen are visible.
        
        Returns:
            bool: True if displayed correctly, False otherwise
        """
        try:
            # Wait for edit_feedback element to be visible using explicit wait
            edit_feedback_element = self.wait.until(
                EC.visibility_of_element_located(self.locators["edit_feedback"])
            )
            
            # Verify edit_feedback is displayed
            if not edit_feedback_element.is_displayed():
                return False
            
            # Optionally verify edit_feedback_char_count is visible as supporting element
            try:
                char_count_element = self.wait.until(
                    EC.visibility_of_element_located(self.locators["edit_feedback_char_count"])
                )
                if not char_count_element.is_displayed():
                    return False
            except TimeoutException:
                pass
            
            # Return True if all key elements are visible
            return True
        except TimeoutException:
            return False

    def verify_experience_textbox_visible(self, timeout=10):
        """
        Verify tell your experience text box is visible.
        Wait for the 'tell your experience' text box element to be visible on the feedback screen.
        
        Args:
            timeout (int): Wait timeout in seconds (default: 10)
        
        Returns:
            bool: True if visible, False otherwise
        """
        try:
            # Wait for edit_feedback element to be visible using explicit wait with configurable timeout
            wait = WebDriverWait(self.driver, timeout)
            edit_feedback_element = wait.until(
                EC.visibility_of_element_located(self.locators["edit_feedback"])
            )
            
            # Return True if edit_feedback is visible
            return edit_feedback_element.is_displayed()
        except TimeoutException:
            return False

    def input_experience_text(self, text: str):
        """
        Input tell your experience text.
        Wait for the experience text box to be clickable, clear any existing text,
        and input the provided text string.
        
        Args:
            text (str): The string to input into the text box
        """
        try:
            # Wait for edit_feedback element to be clickable using explicit wait
            edit_feedback_element = self.wait.until(
                EC.element_to_be_clickable(self.locators["edit_feedback"])
            )
            
            # Clear existing text from edit_feedback
            edit_feedback_element.clear()
            
            # Input the provided text string into edit_feedback
            edit_feedback_element.send_keys(text)
        except TimeoutException as e:
            raise Exception(f"Failed to input experience text: {str(e)}")

    def get_experience_text_value(self):
        """
        Get tell your experience text value.
        Retrieve and return the current text value from the 'tell your experience' text box.
        
        Returns:
            str: The text value from the text box
        """
        try:
            # Wait for edit_feedback element to be present using explicit wait
            edit_feedback_element = self.wait.until(
                EC.presence_of_element_located(self.locators["edit_feedback"])
            )
            
            # Retrieve text value from edit_feedback using get_attribute('value') or text property
            text_value = edit_feedback_element.get_attribute('value')
            if text_value is None:
                text_value = edit_feedback_element.text
            
            # Return the text as a string
            return text_value
        except TimeoutException as e:
            raise Exception(f"Failed to get experience text value: {str(e)}")

    def assert_experience_text_truncated(self, expected_length: int):
        """
        Assert tell your experience text is truncated.
        Verify that the text in the experience text box is truncated to the expected maximum length.
        
        Args:
            expected_length (int): The maximum character length expected after truncation
        
        Raises:
            AssertionError: If the text length doesn't match expected_length
        """
        try:
            # Wait for edit_feedback element to be present
            edit_feedback_element = self.wait.until(
                EC.presence_of_element_located(self.locators["edit_feedback"])
            )
            
            # Get current text value from edit_feedback
            current_text = edit_feedback_element.get_attribute('value')
            if current_text is None:
                current_text = edit_feedback_element.text
            
            # Calculate the length of the retrieved text
            actual_length = len(current_text)
            
            # Assert that the length equals expected_length parameter
            assert actual_length == expected_length, (
                f"Text truncation failed: Expected length {expected_length}, "
                f"but got {actual_length}. Text: '{current_text}'"
            )
            
            # Optionally verify edit_feedback_char_count displays correct count
            try:
                char_count_element = self.wait.until(
                    EC.presence_of_element_located(self.locators["edit_feedback_char_count"])
                )
                char_count_text = char_count_element.text
            except TimeoutException:
                pass
        except TimeoutException as e:
            raise AssertionError(f"Failed to verify text truncation: {str(e)}")

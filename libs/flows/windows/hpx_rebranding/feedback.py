import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys


class FeedbackPage(HPXRebrandingFlow):
    """
    Page Object Model class for Feedback functionality on Windows platform
    """
    flow_name = "feedback"

    def __init__(self, driver):
        """
        Constructor to initialize the FeedbackPage object

        Args:
            driver: WebDriver instance for UI automation
        """
        super().__init__(driver)
        self.driver = driver

    def verify_edit_feedback_screen(self):
        """
        Verify edit feedback screen opens and all key elements are visible

        Returns:
            bool: True if all elements are found

        Raises:
            Exception: If any element is not found within timeout
        """
        self.driver.wait_for_object("hpx_feedback_page_title", timeout=10)
        self.driver.wait_for_object("edit_feedback", timeout=10)
        self.driver.wait_for_object("send_feedback_submit_btn", timeout=10)
        return True

    def input_tell_your_experience_text(self, text):
        """
        Input text into the 'tell your experience' text field

        Args:
            text (str): The text content to input into the experience field
        """
        self.driver.wait_for_object("edit_feedback", timeout=10)
        self.driver.click("edit_feedback", timeout=10)
        edit_feedback_element = self.driver.wait_for_object("edit_feedback", timeout=10)
        edit_feedback_element.send_keys(Keys.CONTROL + "a")
        edit_feedback_element.send_keys(Keys.DELETE)
        self.driver.send_keys("edit_feedback", text, timeout=10)

    def get_tell_your_experience_text_value(self):
        """
        Retrieve the current text value from the 'tell your experience' input field

        Returns:
            str: The current text value in the experience field
        """
        self.driver.wait_for_object("edit_feedback", timeout=10)
        text_value = self.driver.get_attribute("edit_feedback", "Value.Value", timeout=10)
        return text_value if text_value is not None else ""

    def assert_tell_your_experience_text_is_truncated(self, expected_max_length):
        """
        Verify that the text in the 'tell your experience' field has been truncated
        to the expected maximum character length

        Args:
            expected_max_length (int): The maximum allowed character count

        Returns:
            bool: True if all assertions pass

        Raises:
            AssertionError: If the text length does not match expected_max_length
        """
        self.driver.wait_for_object("edit_feedback", timeout=10)
        current_text = self.get_tell_your_experience_text_value()
        actual_length = len(current_text)
        
        self.driver.wait_for_object("edit_feedback_char_count", timeout=10)
        char_count_display = self.driver.get_attribute("edit_feedback_char_count", "Name", timeout=10)
        
        assert actual_length == expected_max_length, (
            f"Text length {actual_length} does not match expected truncated length {expected_max_length}. "
            f"Character count display shows: {char_count_display}"
        )
        
        return True
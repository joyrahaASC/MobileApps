import pytest
from libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


@pytest.mark.usefixtures("windows_test_setup")
class TestFeedback:
    """
    Test Suite for Feedback functionality
    """

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, windows_test_setup):
        """Setup fixture for test class"""
        cls = request.cls
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.flowContainer = cls.fc.fd["flowContainer"]
        cls.feedback = cls.fc.fd["feedback"]

    def test_feedback_text_truncation(self):
        """
        Test Case: Verify feedback text is truncated to 2000 characters
        Steps:
        1. Verify profile icon is visible
        2. Click profile button
        3. Verify feedback button is present
        4. Click feedback button
        5. Verify edit feedback screen is displayed
        6. Input tell your experience text
        7. Get tell your experience text value
        8. Assert tell your experience text is truncated to 2000 characters
        """
        # Step 1: Verify profile icon is visible
        self.flowContainer.click_profile_button()
        
        # Step 2: Click profile button
        self.flowContainer.click_profile_button()
        
        # Step 3: Verify feedback button is present
        self.feedback.verify_feedback_button_present()
        
        # Step 4: Click feedback button
        self.feedback.click_feedback_button()
        
        # Step 5: Verify edit feedback screen is displayed
        self.feedback.verify_edit_feedback()
        
        # Step 6: Input tell your experience text
        self.feedback.input_tell_your_experience()
        
        # Step 7: Get tell your experience text value
        self.feedback.get_entered_text()
        
        # Step 8: Assert tell your experience text is truncated to 2000 characters
        self.feedback.verify_text_truncated_to_max_length()

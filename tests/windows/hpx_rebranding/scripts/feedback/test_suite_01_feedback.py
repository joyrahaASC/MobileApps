import pytest
from libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


class TestFeedback:
    """
    Test suite for feedback functionality
    """

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, windows_test_setup):
        cls = self.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.profile = request.cls.fc.fd["profile"]
        cls.feedback = request.cls.fc.fd["feedback"]

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
        7. Get entered tell your experience value
        8. Assert tell your experience text is truncated to 2000 characters
        """
        # Step 1: Verify profile icon is visible
        self.profile.verify_profile_icon_show_up()
        
        # Step 2: Click profile button
        self.profile.click_devicepage_avatar_btn()
        
        # Step 3: Verify feedback button is present
        self.profile.verify_feedback_btn()
        
        # Step 4: Click feedback button
        self.profile.click_feedback_btn()
        
        # Step 5: Verify edit feedback screen is displayed
        self.feedback.verify_edit_feedback()
        
        # Step 6: Input tell your experience text
        self.feedback.input_tell_your_experience()
        
        # Step 7: Get entered tell your experience value
        self.feedback.get_entered_text()
        
        # Step 8: Assert tell your experience text is truncated to 2000 characters
        self.feedback.assert_tell_your_experience_truncated_to_max_characters()

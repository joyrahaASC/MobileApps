import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_C05(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.feedback = request.cls.fc.fd["feedback"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_verify_feedback_text_truncation_to_2000_characters(self):
        """Test to verify feedback text is truncated to 2000 characters"""
        # Verify profile icon is visible
        assert self.profile.verify_profile_icon_show_up(), "Profile icon is not visible"
        
        # Click profile button
        self.profile.click_profile_icon_show_up()
        
        # Verify feedback button is present
        assert self.profile.verify_feedback_btn(), "Feedback button is not present"
        
        # Click feedback button
        self.profile.click_feedback_btn()
        
        # Verify edit feedback screen is displayed
        assert self.feedback.verify_edit_feedback(), "Edit feedback screen is not displayed"
        
        # Input tell your experience text (more than 2000 characters)
        test_text = "A" * 2500
        self.feedback.input_tell_your_experience(test_text)
        
        # Get entered tell your experience text value
        entered_text = self.feedback.get_entered_text()
        
        # Assert tell your experience text is truncated to 2000 characters
        self.feedback.assert_text_truncated_to_max_characters()
        assert len(entered_text) <= 2000, f"Text not truncated to 2000 characters. Found: {len(entered_text)} characters"

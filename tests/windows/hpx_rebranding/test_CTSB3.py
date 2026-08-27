import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_CTSB3(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.feedback = request.cls.fc.fd["feedback"]

    @pytest.mark.regression
    def test_01_verify_feedback_flow_CTSB3(self):
        assert self.profile.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.profile.verify_feedback_btn(), "feedback button not present"
        self.profile.click_feedback_btn()
        self.profile.click_profile_button()
        self.feedback.input_tell_your_experience()
        entered_text = self.feedback.get_entered_text()
        assert self.feedback.verify_edit_feedback_screen_opens(), "edit feedback screen did not open"
        self.feedback.assert_tell_your_experience_text_is_truncated()

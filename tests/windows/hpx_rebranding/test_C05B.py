import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_C05B(object):
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
    def test_01_verify_profile_and_feedback_flow_C05B(self):
        assert self.profile.verify_profile_icon_show_up(), "Profile icon is not visible"
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_feedback_btn(), "Feedback button is not present"
        self.profile.click_feedback_btn()
        assert self.feedback.verify_edit_feedback(), "Edit feedback screen is not displayed"
        assert self.feedback.verify_tell_your_experience(), "Tell your experience text box is not visible"
        self.feedback.input_tell_your_experience_text()
        entered_text = self.feedback.get_entered_text()
        assert entered_text, "Failed to retrieve entered text from feedback field"

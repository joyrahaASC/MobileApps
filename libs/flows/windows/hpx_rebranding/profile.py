from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time

class Profile(HPXRebrandingFlow):
    flow_name = "profile"

    def click_sign_in_from_avatar_sideflyout(self):
        self.driver.wait_for_object("sideflyout_sign_in_link", timeout=20)
        self.driver.click("sideflyout_sign_in_link")

    def verify_profile_icon_visible(self):
        try:
            self.driver.wait_for_object("profile_icon_signed_in", timeout=10)
            return True
        except:
            return False

    def click_profile_button(self):
        self.driver.wait_for_object("profile_icon_signed_in", timeout=20)
        self.driver.click("profile_icon_signed_in", timeout=10)

    def verify_feedback_button_present(self):
        try:
            self.driver.wait_for_object("feedback_btn", timeout=10, raise_e=False)
            return True
        except:
            return False

    def click_feedback_button(self):
        self.driver.wait_for_object("feedback_btn", timeout=10)
        self.driver.click("feedback_btn", timeout=10)

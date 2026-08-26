from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time

class Profile(HPXRebrandingFlow):
    flow_name = "profile"

    def click_sign_in_from_avatar_sideflyout(self):
        self.driver.wait_for_object("sideflyout_sign_in_link", timeout=20)
        self.driver.click("sideflyout_sign_in_link")

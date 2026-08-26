from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys

class Feedback(HPXRebrandingFlow):
    flow_name = "feedback"

    def click_whats_your_feedback_related_to_options(self):
        self.driver.click("whats_your_feedback_related_to_options", timeout=10)

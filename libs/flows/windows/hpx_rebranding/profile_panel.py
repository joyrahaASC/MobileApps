from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class ProfilePanel(HPXRebrandingFlow):
    flow_name = "profile_panel"

    def click_profile_button(self):
        """
        Wait for the profile button element to be clickable and perform a click action on it.
        This should open or activate the profile interface.
        """
        self.driver.wait_for_object("profile_button")
        self.driver.click("profile_button", timeout=10)

    def verify_feedback_button_present(self):
        """
        Wait for and verify that the feedback button element is present in the DOM.
        Return True if present, False otherwise.
        """
        return self.driver.wait_for_object("feedback_button", raise_e=False, timeout=10) is not False

    def click_feedback_button(self):
        """
        Wait for the feedback button element to be clickable and perform a click action on it.
        This should open the feedback form or dialog.
        """
        self.driver.wait_for_object("feedback_button")
        self.driver.click("feedback_button", timeout=10)

    def assert_feedback_button_present(self):
        """
        Assert that the feedback button element is present in the DOM.
        This method should raise an assertion error if the button is not found.
        """
        element = self.driver.wait_for_object("feedback_button", raise_e=False, timeout=10)
        assert element is not False, "Feedback button is not present in the DOM"
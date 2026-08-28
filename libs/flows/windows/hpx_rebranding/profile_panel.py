from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow


class ProfilePanel(HPXRebrandingFlow):
    flow_name = "profile_panel"

    def click_profile_button(self):
        """
        Wait for the profile button element to be clickable and perform a click action
        to open the profile panel or menu.
        """
        self.driver.click("profile_button", timeout=10)

    def verify_feedback_button_present(self):
        """
        Wait for and verify that the feedback button element is present and visible
        in the profile panel. Return True if present, False otherwise.
        """
        return self.driver.wait_for_object("feedback_button", raise_e=False, timeout=10) is not False

    def click_feedback_button(self):
        """
        Wait for the feedback button element to be clickable and perform a click action
        to navigate to the feedback screen.
        """
        self.driver.click("feedback_button", timeout=10)

    def verify_profile_icon_visible(self):
        """
        Wait for the profile icon element to be visible on the devices MFE interface
        and verify its display state. Return True if visible, False otherwise.
        """
        return self.driver.wait_for_object("profile_button", raise_e=False, timeout=10) is not False

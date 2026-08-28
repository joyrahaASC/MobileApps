from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class DevicesMFE(HPXRebrandingFlow):
    flow_name = "devices_mfe"

    def __init__(self, driver):
        super().__init__(driver)

    def click_profile_button(self):
        """
        Wait for the profile button/icon to be clickable and click it to open the profile panel or menu.
        """
        self.driver.wait_for_object("profile_button", timeout=10)
        self.driver.click("profile_button", timeout=10)
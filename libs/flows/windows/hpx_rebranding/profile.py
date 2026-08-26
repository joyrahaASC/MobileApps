from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time

class Profile(HPXRebrandingFlow):
    flow_name = "profile"

    def click_sign_in_from_avatar_sideflyout(self):
        self.driver.wait_for_object("sideflyout_sign_in_link", timeout=20)
        self.driver.click("sideflyout_sign_in_link")

    def verify_profile_icon_visible(self, timeout=10):
        """
        Wait for the profile icon element to be visible on the screen.
        
        Args:
            timeout (int): Maximum time to wait for element visibility. Default is 10 seconds.
            
        Returns:
            bool: True if profile_icon_signed_in is visible within timeout, False otherwise.
        """
        try:
            self.driver.wait_for_object("profile_icon_signed_in", timeout=timeout)
            return True
        except:
            return False

    def verify_feedback_button_present(self, timeout=10):
        """
        Wait for the feedback button element to be present in the DOM.
        
        Args:
            timeout (int): Maximum time to wait for element presence. Default is 10 seconds.
            
        Returns:
            bool: True if feedback_btn is present in DOM within timeout, False otherwise.
        """
        try:
            self.driver.wait_for_object("feedback_btn", timeout=timeout)
            return True
        except:
            return False

    def click_feedback_button(self):
        """
        Wait for the feedback button to be clickable and click it.
        Handles potential overlays or loading states and navigates to the feedback screen.
        
        Raises:
            Exception: If element is not clickable or timeout occurs.
        """
        try:
            self.driver.wait_for_object("feedback_btn", timeout=10)
            self.driver.click("feedback_btn")
        except Exception as e:
            raise Exception(f"Failed to click feedback button: {str(e)}")

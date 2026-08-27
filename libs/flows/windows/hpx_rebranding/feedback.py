from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys

class Feedback(HPXRebrandingFlow):
    flow_name = "feedback"

    def verify_feedback_slide_title(self):
        return self.driver.wait_for_object("hpx_feedback_page_title")

    def verify_menu_btn_from_feedback(self):
        return self.driver.wait_for_object("menu_btn_from_feedback")

    def verify_rating_star_field(self):
        return self.driver.wait_for_object("rating_star_field")

    def verify_why_did_you_open_app_today_title(self):
        return self.driver.wait_for_object("why_did_you_open_app_today_title")

    def verify_why_did_you_open_today_options_text(self):
        return self.driver.wait_for_object("why_did_you_open_today_options")

    def verify_why_did_you_open_app_today_list(self):
        self.click_why_did_you_open_today_options()
        self.verify_get_tech_support()
        self.verify_configure_my_devices()
        self.verify_set_up_my_printer()
        self.verify_print_or_scan()
        self.verify_manage_my_account_feedback()
        self.verify_manage_my_subscriptions()
        self.verify_other_1st_dropdown()

    def verify_get_tech_support(self):
        return self.driver.wait_for_object("get_tech_support")

    def verify_configure_my_devices(self):
        return self.driver.wait_for_object("configure_my_devices")

    def verify_set_up_my_printer(self):
        return self.driver.wait_for_object("set_up_my_printer")

    def verify_print_or_scan(self):
        self.driver.swipe("configure_my_devices")
        return self.driver.wait_for_object("print_or_scan")

    def verify_manage_my_account_feedback(self):
        self.driver.swipe("manage_my_account_feedback")
        return self.driver.wait_for_object("manage_my_account_feedback")

    def verify_manage_my_subscriptions(self):
        self.driver.swipe("manage_my_subscriptions")
        return self.driver.wait_for_object("manage_my_subscriptions")

    def verify_other_1st_dropdown(self):
        self.driver.swipe("other_1st_dropdown")
        return self.driver.wait_for_object("other_1st_dropdown")

    def verify_whats_your_feedback_related_to_title(self):
        return self.driver.wait_for_object("whats_your_feedback_related_to_title")

    def verify_whats_your_feedback_related_to_list(self):
        self.click_whats_your_feedback_related_to_options()
        self.verify_load_time()
        self.verify_ease_of_use()
        self.verify_bug_or_issue()
        self.verify_app_feature_request()
        self.verify_other_2nd_dropdown()
        self.click_whats_your_feedback_related_to_options()

    def verify_load_time(self):
        return self.driver.wait_for_object("load_time")

    def verify_ease_of_use(self):
        return self.driver.wait_for_object("ease_of_use")

    def verify_bug_or_issue(self):
        return self.driver.wait_for_object("bug_or_issue")

    def verify_app_feature_request(self):
        self.driver.swipe("app_feature_request")
        return self.driver.wait_for_object("app_feature_request")

    def verify_other_2nd_dropdown(self):
        self.driver.swipe("other_2nd_dropdown")
        return self.driver.wait_for_object("other_2nd_dropdown")

    def verify_tell_your_experience(self):
        return self.driver.wait_for_object("tell_your_experience_title")

    def verify_edit_feedback(self):
        self.driver.swipe("edit_feedback")
        return self.driver.wait_for_object("edit_feedback")

    def verify_contacting_email(self):
        self.driver.swipe("contacting_email")
        return self.driver.wait_for_object("contacting_email")

    def verify_send_feedback_submit_is_clickbale(self):
        self.driver.swipe("send_feedback_submit_btn")
        if self.driver.wait_for_object("send_feedback_submit_btn").is_enabled():
            return True
        else:
            return False

    def verify_send_feedback_submit_btn(self):
        self.driver.swipe("send_feedback_submit_btn")
        return self.driver.wait_for_object("send_feedback_submit_btn")

    def veify_hp_privacy_statement_link(self):
        self.driver.swipe("hp_privacy_statement_link")
        return self.driver.wait_for_object("hp_privacy_statement_link")

    def verify_feedback_submission_success_message(self):
        self.driver.wait_for_object("feedback_submission_success_message", timeout=15)
        return self.driver.get_attribute("feedback_submission_success_message", "Name", timeout=15)

    def is_cleared(self, object_name):
        """
        Check if the input field is cleared (empty).
        
        :param object_name: The name of the object to check
        :return: True if the field is empty, False otherwise
        """
        self.driver.swipe(object_name, direction="down")
        element = self.driver.wait_for_object(object_name)
        return element.get_attribute("Value.Value") == None

    def verify_no_option_selected(self, dropdown_name):
        """
        Verify that no option is selected in the dropdown.

        :param dropdown_name: The name of the dropdown object to check
        :return: True if no option is selected, False otherwise
        """
        element = self.driver.wait_for_object(dropdown_name)
        selected_value = element.get_attribute("Value.Value")  # Get the current value of the dropdown
        return selected_value == "" or selected_value == "Select an option"

    def verify_after_submission_inputs_cleared(self):
        assert self.verify_no_option_selected("why_did_you_open_today_options")
        assert self.verify_no_option_selected("whats_your_feedback_related_to_options")
        assert self.is_cleared("edit_feedback")

    def select_each_option_from_first_dropdown_menu(self):
        self.click_why_did_you_open_today_options()
        self.driver.swipe(distance=5, direction="up")
        self.driver.click("get_tech_support")
        self.click_why_did_you_open_today_options()
        self.driver.click("configure_my_devices")
        self.click_why_did_you_open_today_options()
        self.driver.click("set_up_my_printer")
        self.click_why_did_you_open_today_options()
        self.driver.click("print_or_scan")
        self.click_why_did_you_open_today_options()
        self.driver.swipe("manage_my_account_feedback")
        self.driver.click("manage_my_account_feedback")
        self.click_why_did_you_open_today_options()
        self.driver.swipe("other_1st_dropdown")
        self.driver.click("manage_my_subscriptions")
        self.click_why_did_you_open_today_options()
        self.driver.swipe("other_1st_dropdown")
        self.driver.click("other_1st_dropdown")

    def verify_submit_btn_position(self, tolerance=100):
        """
        Verify the position of the submit button.
        :return: True if the submit button is in the expected position, False otherwise
        """
        self.driver.swipe("send_feedback_submit_btn", direction="down")
        element = self.driver.wait_for_object("send_feedback_submit_btn", timeout=10)
        expected_position = (1300, 900)
        actual_position = (element.location['x'], element.location['y'])
        x_diff = abs(actual_position[0] - expected_position[0])
        y_diff = abs(actual_position[1] - expected_position[1])
        return x_diff <= tolerance and y_diff <= tolerance

    def get_entered_text(self):
        return self.driver.get_attribute("edit_feedback", "Value.Value")

    def select_each_option_from_second_dropdown_menu(self):
        self.driver.swipe(distance=11)
        self.click_whats_your_feedback_related_to_options()
        self.driver.wait_for_object("load_time")
        self.driver.click("load_time", timeout=10)
        self.click_whats_your_feedback_related_to_options()
        self.driver.click("ease_of_use", timeout=10)
        self.click_whats_your_feedback_related_to_options()
        self.driver.click("bug_or_issue", timeout=10)
        self.click_whats_your_feedback_related_to_options()
        self.driver.click("app_feature_request", timeout=10)
        self.click_whats_your_feedback_related_to_options()
        self.driver.click("other_2nd_dropdown", timeout=10)

    def verify_hpx_feedback_page_title(self):
        return self.driver.get_attribute("hpx_feedback_page_title", "Name")

    def verify_stars_present(self):
        return self.driver.wait_for_object("rating_star", timeout=10)

    def get_invalid_email_message(self):
        return self.driver.get_attribute("invalid_email_message", "Name")

    ############################################# Action flows #############################################

    def click_menu_btn_from_feedback(self):
        self.driver.click("menu_btn_from_feedback", timeout=10)

    def click_rating_star(self):  # it will click 1st star
        self.driver.click("rating_star", timeout=10)

    def select_star_rating(self, rating):
        for i in range(1, rating):
            self.driver.click(f"{i}_star", timeout=10)

    def select_and_unselect_star_rating(self, rating):
        for i in range(1, rating + 1):
            self.driver.click(f"{i}_star", timeout=10)
            self.driver.click(f"{i}_star", timeout=10)

    def unselect_star_rating(self, rating):
        for i in range(rating, 0, -1):
            self.driver.click(f"{i}_star", timeout=10)
            if i == 1:
                self.driver.click("1_star")

    def click_why_did_you_open_today_options(self):
        self.driver.wait_for_object("why_did_you_open_today_options", timeout=20)
        self.driver.click("why_did_you_open_today_options", timeout=10)

    def select_get_tech_support(self):
        self.driver.click("get_tech_support", timeout=10)

    def select_configure_my_devices(self):
        self.driver.click("configure_my_devices", timeout=10)

    def select_set_up_my_printer(self):
        self.driver.click("set_up_my_printer", timeout=10)

    def select_print_or_scan(self):
        self.driver.click("print_or_scan", timeout=10)

    def select_manage_my_account_feedback(self):
        self.driver.swipe(distance=2)
        self.driver.click("manage_my_account_feedback", timeout=10)

    def select_manage_my_subscriptions(self):
        self.driver.swipe("other_1st_dropdown")
        self.driver.click("manage_my_subscriptions", timeout=10)

    def select_other_1st_dropdown_feedback(self):
        self.driver.swipe("other_1st_dropdown", distance=6)
        self.driver.click("other_1st_dropdown", timeout=10)

    def click_whats_your_feedback_related_to_options(self):
        self.driver.click("whats_your_feedback_related_to_options", timeout=10)

    def select_load_time(self):
        self.driver.click("load_time", timeout=10)

    def select_erase_of_use(self):
        self.driver.click("ease_of_use", timeout=10)

    def select_bug_or_issue(self):
        self.driver.click("bug_or_issue", timeout=10)

    def select_app_feature_request(self):
        self.driver.swipe("app_feature_request")
        self.driver.click("app_feature_request", timeout=10)

    def select_other_2nd_dropdown_feedback(self):
        self.driver.swipe("other_2nd_dropdown")
        self.driver.click("other_2nd_dropdown", timeout=10)

    def input_tell_your_experience(self, experience):
        self.driver.send_keys("edit_feedback","[test] [internal_testing] " + experience)

    def input_contacting_email(self, email):
        self.driver.send_keys("contacting_email", email)

    def click_submit_feedback(self):
        self.driver.swipe(distance=11)
        self.driver.click("send_feedback_submit_btn", timeout=10)

    def click_hp_privacy_statement_link(self):
        self.driver.click("hp_privacy_statement_link", timeout=10)

    def handle_feature_feedback_popup(self):
        if self.driver.wait_for_object("feature_feedback_popup", raise_e=False, timeout=10) is not False:
            self.driver.click("feature_feedback_popup")

    def terminate_hp_app_with_alt_f4(self):
        alt_f4_element = self.driver.wait_for_object("edit_feedback")
        alt_f4_element.click()
        alt_f4_element.send_keys(Keys.ALT + Keys.F4)

    def get_feedback_text_char_count(self, timeout=10):
        char_count_text = self.driver.get_attribute("edit_feedback_char_count", "Name", timeout=timeout)
        return char_count_text

    def assert_text_truncated_to_max_characters(self, expected_max_length: int = 2000) -> bool:
        """
        Assert that the feedback text is truncated to the maximum allowed characters.
        
        :param expected_max_length: The maximum allowed character length (default: 2000)
        :return: True if the text is properly truncated to max length
        :raises AssertionError: If the text length exceeds the expected maximum or doesn't match expected truncation
        """
        # Wait for the edit_feedback element to be present
        self.driver.wait_for_object("edit_feedback")
        
        # Retrieve the current text from the feedback field
        actual_text = self.get_entered_text()
        
        # Handle edge case: if actual_text is None or empty
        if actual_text is None or actual_text == "":
            print(f"Warning: Feedback text field is empty or None")
            actual_text = "" if actual_text is None else actual_text
        
        # Calculate the actual character count
        actual_length = len(actual_text)
        print(f"Actual character count: {actual_length}, Maximum allowed: {expected_max_length}")
        
        # Wait for the character count display element
        self.driver.wait_for_object("edit_feedback_char_count")
        
        # Get the character count display text
        char_count_display = self.driver.get_attribute("edit_feedback_char_count", "Name")
        print(f"Character count display: {char_count_display}")
        
        # Parse the character count display (e.g., from '2000/2000' format)
        if char_count_display and "/" in char_count_display:
            displayed_count = int(char_count_display.split("/")[0])
            print(f"Parsed displayed count: {displayed_count}")
            
            # Verify that the character count display matches the actual text length
            assert displayed_count == actual_length, f"Character count display ({displayed_count}) does not match actual text length ({actual_length})"
        
        # Assert that the text length does not exceed the expected maximum
        assert actual_length <= expected_max_length, f"Text length ({actual_length}) exceeds maximum allowed length ({expected_max_length})"
        
        # Assert that the text length equals the expected maximum for truncation verification
        assert actual_length == expected_max_length, f"Text was not truncated to maximum length. Expected: {expected_max_length}, Actual: {actual_length}"
        
        print(f"Assertion passed: Text is properly truncated to {expected_max_length} characters")
        return True

    def verify_edit_feedback_screen_opens(self):
        """
        Verify that the edit feedback screen is displayed after clicking the feedback button.
        Checks for the presence of key elements such as the feedback slide title, the 'tell your experience' text field,
        dropdown menus for feedback categories, and the submit button.
        
        :return: True if all required elements are visible, False otherwise
        """
        try:
            # Wait for feedback page title to be visible
            self.driver.wait_for_object("hpx_feedback_page_title", timeout=10)
            
            # Wait for rating star field to be visible
            self.driver.wait_for_object("rating_star_field", timeout=10)
            
            # Wait for 'why did you open app today' title to be visible
            self.driver.wait_for_object("why_did_you_open_app_today_title", timeout=10)
            
            # Wait for 'why did you open today' options dropdown to be visible
            self.driver.wait_for_object("why_did_you_open_today_options", timeout=10)
            
            # Wait for 'what's your feedback related to' title to be visible
            self.driver.wait_for_object("whats_your_feedback_related_to_title", timeout=10)
            
            # Wait for 'what's your feedback related to' options dropdown to be visible
            self.driver.wait_for_object("whats_your_feedback_related_to_options", timeout=10)
            
            # Swipe to 'tell your experience' title if needed
            self.driver.swipe("tell_your_experience_title")
            
            # Wait for 'tell your experience' title to be visible
            self.driver.wait_for_object("tell_your_experience_title", timeout=10)
            
            # Swipe to edit feedback field
            self.driver.swipe("edit_feedback")
            
            # Wait for edit feedback field to be visible
            self.driver.wait_for_object("edit_feedback", timeout=10)
            
            # Swipe to submit button
            self.driver.swipe("send_feedback_submit_btn")
            
            # Wait for submit button to be visible
            self.driver.wait_for_object("send_feedback_submit_btn", timeout=10)
            
            # All elements successfully found
            return True
            
        except Exception as e:
            # Handle exceptions and return False if any element fails to load
            print(f"Error verifying edit feedback screen: {str(e)}")
            return False

    def assert_tell_your_experience_text_is_truncated(self, expected_max_length=1000):
        """
        Verify that the text entered in the 'tell your experience' field is truncated to the maximum allowed character limit.
        
        :param expected_max_length: The maximum allowed character length (default: 1000)
        :raises AssertionError: If the text is not properly truncated or if the character count is incorrect
        """
        # Swipe to edit_feedback if needed to bring element into view
        self.driver.swipe("edit_feedback")
        
        # Wait for edit_feedback to be visible
        self.driver.wait_for_object("edit_feedback", timeout=10)
        
        # Call existing get_entered_text() method to retrieve current text value
        actual_text = self.get_entered_text()
        
        # Handle None or empty text
        if actual_text is None:
            actual_text = ""
        
        # Calculate the length of the retrieved text value
        actual_length = len(actual_text)
        
        # Assert that the calculated length is less than or equal to expected_max_length
        assert actual_length <= expected_max_length, f"Text length ({actual_length}) exceeds maximum allowed length ({expected_max_length})"
        
        # Wait for edit_feedback_char_count to be visible
        self.driver.wait_for_object("edit_feedback_char_count", timeout=10)
        
        # Get the character count display text from edit_feedback_char_count
        char_count_display = self.driver.get_attribute("edit_feedback_char_count", "Name")
        
        # Parse the character count display text to extract current count value
        if char_count_display and "/" in char_count_display:
            displayed_count = int(char_count_display.split("/")[0])
            
            # Assert that the current count from display matches the actual text length
            assert displayed_count == actual_length, f"Character count display ({displayed_count}) does not match actual text length ({actual_length})"
            
            # Assert that the current count does not exceed expected_max_length
            assert displayed_count <= expected_max_length, f"Character count display ({displayed_count}) exceeds maximum allowed length ({expected_max_length})"
        else:
            # Raise AssertionError if character count display format is incorrect
            raise AssertionError(f"Character count display format is incorrect: {char_count_display}")

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

    def assert_tell_your_experience_truncated_to_max_characters(self, expected_max_length=2000):
        """
        Assert that the tell your experience text is truncated to the maximum character limit.
        
        :param expected_max_length: The expected maximum character length (default 2000)
        :return: True if all assertions pass successfully
        :raises AssertionError: If text length exceeds maximum or truncation did not occur as expected
        """
        # Wait for edit_feedback element to be present
        self.driver.wait_for_object('edit_feedback')
        
        # Call existing method to retrieve the current text value from the feedback text field
        entered_text = self.get_entered_text()
        
        # Calculate the actual character length
        actual_length = len(entered_text)
        
        # Wait for edit_feedback_char_count element to be present
        self.driver.wait_for_object('edit_feedback_char_count')
        
        # Get the character count display text
        char_count_display = self.driver.get_attribute('edit_feedback_char_count', 'Name')
        
        # Parse the character count display to extract current count (e.g., from '2000/2000' format)
        if '/' in char_count_display:
            current_count_str = char_count_display.split('/')[0].strip()
            try:
                current_count = int(current_count_str)
            except ValueError:
                raise AssertionError(f"Unable to parse character count from display: {char_count_display}")
        else:
            raise AssertionError(f"Character count display format is unexpected: {char_count_display}")
        
        # Assert that actual length does not exceed expected_max_length
        if actual_length > expected_max_length:
            raise AssertionError(
                f"Text length {actual_length} exceeds the maximum allowed length of {expected_max_length}"
            )
        
        # Assert that actual length equals expected_max_length when truncation should have occurred
        if actual_length != expected_max_length:
            raise AssertionError(
                f"Text length {actual_length} does not equal expected maximum length {expected_max_length}. "
                f"Truncation may not have occurred as expected."
            )
        
        # Assert that the character count display shows the correct format indicating truncation occurred
        if current_count != expected_max_length:
            raise AssertionError(
                f"Character count display shows {current_count} but expected {expected_max_length}"
            )
        
        # Return True if all assertions pass successfully
        return True

    def verify_feedback_button_present(self):
        """
        Wait for and verify that the feedback button is present and visible in the UI.
        
        :return: Element object if present, raises exception otherwise
        """
        element = self.driver.wait_for_object('menu_btn_from_feedback')
        if element is None or element is False:
            raise AssertionError("Feedback button 'menu_btn_from_feedback' is not present")
        return element

    def click_feedback_button(self):
        """
        Wait for the feedback button to be clickable and click it to open the feedback form or dialog.
        
        :return: None
        """
        self.driver.wait_for_object('menu_btn_from_feedback', timeout=10)
        self.driver.click('menu_btn_from_feedback', timeout=10)

    def verify_feedback_title_displayed(self, expected_title='Why did you open the app today?'):
        """
        Wait for and verify that the feedback form title matches the expected text.
        
        :param expected_title: The expected title text (default: 'Why did you open the app today?')
        :return: True if title matches expected text
        :raises AssertionError: If title does not match expected text
        """
        self.driver.wait_for_object('why_did_you_open_app_today_title')
        actual_title = self.driver.get_attribute('why_did_you_open_app_today_title', 'Name')
        
        if actual_title != expected_title:
            raise AssertionError(
                f"Feedback title mismatch. Expected: '{expected_title}', but got: '{actual_title}'"
            )
        
        return True

    def verify_options_list_visible(self):
        """
        Wait for and verify that the options list is visible below the feedback title.
        
        :return: Element object if visible, raises exception otherwise
        """
        element = self.driver.wait_for_object('why_did_you_open_today_options', timeout=20)
        if element is None or element is False:
            raise AssertionError("Options list 'why_did_you_open_today_options' is not visible")
        return element

    def verify_text_truncated_to_max_length(self, expected_length=2000):
        """
        Get the current text from the tell your experience field using get_entered_text() and verify 
        that its length does not exceed the specified maximum length (default 2000 characters). 
        Return True if text is properly truncated, False otherwise.
        
        :param expected_length: The expected maximum character length (default 2000)
        :return: True if text is properly truncated
        :raises AssertionError: If text length exceeds maximum or truncation validation fails
        """
        # Wait for edit_feedback element to be present
        self.driver.wait_for_object('edit_feedback')
        
        # Call existing method to retrieve the current text value from the feedback text field
        entered_text = self.get_entered_text()
        
        # Calculate the actual character length
        actual_length = len(entered_text)
        
        # Wait for edit_feedback_char_count element to be present
        self.driver.wait_for_object('edit_feedback_char_count')
        
        # Get the character count display text
        char_count_display = self.driver.get_attribute('edit_feedback_char_count', 'Name')
        
        # Parse the character count display to extract current count (e.g., from '2000/2000' format)
        if '/' in char_count_display:
            current_count_str = char_count_display.split('/')[0].strip()
            try:
                current_count = int(current_count_str)
            except ValueError:
                raise AssertionError(f"Unable to parse character count from display: {char_count_display}")
        else:
            raise AssertionError(f"Character count display format is unexpected: {char_count_display}")
        
        # Assert that actual text length does not exceed expected_length parameter
        if actual_length > expected_length:
            raise AssertionError(
                f"Text length {actual_length} exceeds the maximum allowed length of {expected_length}"
            )
        
        # Assert that actual text length equals expected_length when truncation should have occurred
        if actual_length != expected_length:
            raise AssertionError(
                f"Text length {actual_length} does not equal expected maximum length {expected_length}. "
                f"Truncation may not have occurred as expected."
            )
        
        # Assert that the character count display shows the correct format indicating truncation occurred
        if current_count != expected_length:
            raise AssertionError(
                f"Character count display shows {current_count} but expected {expected_length}"
            )
        
        # Return True if all assertions pass successfully
        return True
def test_forward_to_services_page(landing_page):
    services_page = landing_page.select_services_menu()
    assert services_page.get_current_url() == services_page.url


def test_forward_to_talk_to_qa_experts_page(landing_page):
    services_page = landing_page.select_services_menu()
    contact_us_page = services_page.select_talk_button()
    assert contact_us_page.get_current_url() == contact_us_page.url


def test_forward_to_talk_to_qa_experts_form_visible(landing_page):
    services_page = landing_page.select_services_menu()
    contact_us_page = services_page.select_talk_button()
    assert contact_us_page.get_form_title() == "Learn More About Test IO"


def test_fill_learn_more_about_test_io_form_with_not_valid_email(landing_page, user):
    services_page = landing_page.select_services_menu()
    contact_us_page = services_page.select_talk_button()
    contact_us_page.fill_form_field('first name', user.first_name)
    contact_us_page.fill_form_field('last name', user.last_name)
    contact_us_page.fill_form_field('company', user.company)
    contact_us_page.fill_form_field('message', user.message)
    contact_us_page.fill_form_field('email', user.incorrect_email)
    contact_us_page.click_on_talk_to_qa_experts_button()
    assert contact_us_page.get_form_title() == "Learn More About Test IO"


def test_fill_learn_more_about_test_io_form_clear_and_return_to_service_page(landing_page, user):
    services_page = landing_page.select_services_menu()
    contact_us_page = services_page.select_talk_button()
    contact_us_page.fill_form_field('first name', user.first_name)
    contact_us_page.fill_form_field('last name', user.last_name)
    contact_us_page.fill_form_field('company', user.company)
    contact_us_page.fill_form_field('message', user.message)
    contact_us_page.fill_form_field('email', user.email)
    for field in ['first name', 'last name', 'company', 'message', 'email']:
        contact_us_page.clear_field_by_name(field)
    contact_us_page.click_on_talk_to_qa_experts_button()
    contact_us_page.switch_to_first_window()
    assert services_page.get_current_url() == services_page.url


def test_check_terms_and_conditions_link(landing_page):
    services_page = landing_page.select_services_menu()
    contact_us_page = services_page.select_talk_button()
    policies_page = contact_us_page.click_on_term_link()
    assert policies_page.get_current_url() == policies_page.url


def test_scroll_page_and_check_footer_menu(landing_page):
    landing_page.scroll_page_to_end()
    assert landing_page.get_become_a_tester_text() == "Become a Tester"


def test_scroll_page_and_forward_to_sign_in_page(landing_page):
    landing_page.scroll_page_to_end()
    sign_in_page = landing_page.select_sign_in_menu()
    assert sign_in_page.get_current_url() == sign_in_page.url


def test_forward_to_sign_in_page_fill_sign_in_form_check_alert_message(landing_page, user):
    sign_in_page = landing_page.select_sign_in_button()
    sign_in_page.switch_to_second_window()
    sign_in_page.fill_sign_in_field('email', user.email)
    sign_in_page.fill_sign_in_field('password', user.password)
    sign_in_page.click_on_submit_button()
    assert sign_in_page.get_alert_message() == "Invalid Email or password."


def test_return_all_cookies_in_pages_and_check_domain_in_cookies(landing_page):
    cookie_from_first_page = landing_page.local_storage.get_current_page_cookie_from_local_storage()
    sign_in_page = landing_page.select_sign_in_button()
    cookie_from_second_page = sign_in_page.local_storage.get_current_page_cookie_from_local_storage()
    sign_in_page.switch_to_second_window()
    reset_password_page = sign_in_page.click_on_reset_password_link()
    cookie_from_third_page = reset_password_page.local_storage.get_current_page_cookie_from_local_storage()
    cookies = cookie_from_first_page, cookie_from_second_page, cookie_from_third_page
    check_domain = 'test.io', 'cirro.io', 'cirro.io'
    for index in range(len(cookies)):
        assert check_domain[index] in cookies[index]


def test_forward_to_sign_in_page_and_reset_password_page(landing_page):
    sign_in_page = landing_page.select_sign_in_button()
    sign_in_page.switch_to_second_window()
    reset_password_page = sign_in_page.click_on_reset_password_link()
    assert reset_password_page.get_page_header() == "Reset password"

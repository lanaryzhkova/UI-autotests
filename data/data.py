class PageUrls:
    """Ссылки на страницы системы"""
    BASE_URL="https://www.way2automation.com/"
    LIFETIME_MEMBERSHIP_URL = BASE_URL + "lifetime-membership-club/"
    LOGIN_URL = BASE_URL + "angularjs-protractor/registeration/#/login"
    LOGIN_RESULT_URL = BASE_URL + "angularjs-protractor/registeration/#/"
    BANKING_APP_URL = BASE_URL + "angularjs-protractor/banking/#/login"
    SAMPLE_FORM_URL = BASE_URL + "angularjs-protractor/banking/registrationform.html"
    BANK_MANAGER_URL = BASE_URL + "angularjs-protractor/banking/#/manager"
    ADD_CUSTOMER_URL = BASE_URL + "angularjs-protractor/banking/#/manager/addCust"
    OPEN_ACCOUNT_URL = BASE_URL + "angularjs-protractor/banking/#/manager/openAccount"
    CUSTOMER_LOGIN_URL = BASE_URL + "angularjs-protractor/banking/#/customer"
    CUSTOMER_ACCOUNT_URL = BASE_URL + "angularjs-protractor/banking/#/account"
    CUSTOMERS_URL = BASE_URL + "angularjs-protractor/banking/#/manager/list"

expected_contact_links = [
                          "https://wa.me/+919711111558", 
                          "https://wa.me/+919711191558", 
                          "tel:+16464800603",
                          "skype:seleniumcoaching?chat",
                          "mailto:trainer@way2automation.com"
                     ]

expected_social_links = [
                          "https://www.facebook.com/way2automation", 
                          "https://in.linkedin.com/in/rahul-arora-0490b751", 
                          "https://plus.google.com/u/0/+RamanAhujatheseleniumguru", 
                          "https://www.youtube.com/c/seleniumappiumtutorialtraining"
                     ]

expected_about_us_info = [
                          "CDR Complex, 3rd Floor, Naya Bans Market, Sector 15, Noida, Near sec-16 Metro Station", 
                          "+91 97111-11-558",
                          "+91 97111-91-558",
                          "trainer@way2automation.com",
                          "seleniumcoaching@gmail.com"
                          ]

expected_navigation_links = [
                             "All Courses"
                            ]

expected_submenu_links = [
                          "Lifetime Membership"
                         ]

valid_user = {
    "username": "angular",
    "password": "password",
    "description": "test user"
}

not_valid_user = {
    "username": "invalid_user",
    "password": "invalid_password",
    "description": "invalid test user"
}

sample_form_user = {
    "first_name": "Test",
    "last_name": "User",
    "email": "test@test.com",
    "password": "Test123",
    "hobbies": ["Sports"],
    "gender": "Male",
    "about": "" 
    }

customer = {
    "first_name": "Test",
    "last_name": "Customer",
    "postcode": "12345"
}


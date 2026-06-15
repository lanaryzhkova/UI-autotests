from selenium.webdriver.common.by import By


class BankingManagerPageLocators:
    ADD_CUSTOMER_BUTTON = (By.XPATH, "//*[contains(text(), 'Add Customer')]")
    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(text(), 'Open Account')]")
    CUSTOMERS_BUTTON = (By.XPATH, "//*[contains(text(), 'Customers')]")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='Last Name']")
    POSTCODE_INPUT = (By.XPATH, "//input[@placeholder='Post Code']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search Customer']")
    ADD_CUSTOMER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Add Customer']")
    CUSTOMER_SELECT = (By.ID, "userSelect")
    CURRENCY_SELECT = (By.ID, "currency")
    PROCESS_BUTTON = (By.XPATH, "//button[text()='Process']")
    CUSTOMER_ROW = (By.TAG_NAME, "tr")
    DELETE_CUSTOMER_BUTTON = (By.XPATH, ".//button[text()='Delete']")
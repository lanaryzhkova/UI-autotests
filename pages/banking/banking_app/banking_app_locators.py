from selenium.webdriver.common.by import By


class BankingAppPageLocators:
    """Локаторы для BankingApp"""

    SAMPLE_FORM_BUTTON = (By.XPATH, "//*[contains(text(), 'Sample Form')]")
    BANK_MANAGER_LOGIN_BUTTON = (
        By.XPATH,
        "//*[contains(text(), 'Bank Manager Login')]",
    )
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//*[contains(text(), 'Customer Login')]")

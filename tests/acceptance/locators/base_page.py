from selenium.webdriver.common.by import By


class BasePageLocators:

    # Use selenium's .find_element(By.TAG_NAME, 'tag_name') or .find_element_by_id(By.ID, 'element_id') to find element

    TITLE = By.TAG_NAME, 'h1'
    NAV_LINKS = By.CLASS_NAME, 'nav-link'

from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class HomePageLocators(BasePageLocators):

    # Use selenium's .find_element(By.TAG_NAME, 'tag_name') or .find_element_by_id(By.ID, 'element_id') to find element
    NAVIGATION_LINK = By.ID, 'blog-link'
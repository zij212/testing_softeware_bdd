from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class BlogPageLocators(BasePageLocators):

    # Use selenium's .find_element(By.TAG_NAME, 'tag_name') or .find_element_by_id(By.ID, 'element_id') to find element
    ADD_POST_LINK = By.ID, 'add-post-link'
    POSTS_SECTION = By.ID, 'posts'
    POST = By.CLASS_NAME, 'post-link'


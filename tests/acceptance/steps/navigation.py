from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    # user context.driver to pass the same browser page to the next testing step
    context.driver = webdriver.Chrome(
        'C:/Projects/ZJ/Udemy/automated_software_testing/section10_acceptance_testing/chromedriver_win32/chromedriver')
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(
        'C:/Projects/ZJ/Udemy/automated_software_testing/section10_acceptance_testing/chromedriver_win32/chromedriver')
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    # this function in renamed by the decorator
    page = BlogPage(context.driver)
    expected_url = page.url

    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    page = HomePage(context.driver)
    expected_url = page.url  # need the trailing / otherwise assertion will fail
    assert context.driver.current_url == expected_url


@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome(
        'C:/Projects/ZJ/Udemy/automated_software_testing/section10_acceptance_testing/chromedriver_win32/chromedriver')
    page = NewPostPage(context.driver)
    context.driver.get(page.url)








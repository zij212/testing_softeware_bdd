# testing_software_bdd

This repo is from following Section 10 of the [Automated Software Testing with Python](https://www.udemy.com/course/automated-software-testing-with-python/) class on Udemy. It covers Behavior Driven Development (BDD)

Given a simple flask app and html templates, we test what actions user can take and the outcomes of the action.

Here is the final stucture of the tests folder
```
│   __init__.py
│
└───acceptance
    │   content.feature
    │   navigation.feature
    │   __init__.py
    │
    ├───locators
    │       base_page.py
    │       blog_page.py
    │       home_page.py
    │       new_post_page.py
    │       __init__.py
    │
    ├───page_model
    │       base_page.py
    │       blog_page.py
    │       home_page.py
    │       new_post_page.py
    │       __init__.py
    │
    └───steps
            content.py
            interactions.py
            navigation.py
            waits.py
            __init__.py
```

Before running the tests, we need to install the behave and selenimum package in the virtual environment and the Gherkin and MultiRun plugin in PyCharm

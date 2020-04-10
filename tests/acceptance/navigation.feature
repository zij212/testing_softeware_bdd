Feature: Test navigation between pages
    we can have a longer decription
    That can span a few lines

    Scenario: Homepage can go to Blog
      Given I am on the homepage
#      When I click on the link with id "blog-link"
      When I click on the "Go to blog" link
      Then I am on the blog page

    Scenario: Blog can go to Homepage
      Given I am on the blog page
#      When I click on the link with id "home-link"
      When I click on the "Go to home" link
      Then I am on the homepage
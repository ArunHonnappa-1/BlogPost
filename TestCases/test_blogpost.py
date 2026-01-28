import pytest
import time
import string
import random
from selenium import webdriver
from PageObjects.blogpost_practice import Practice
from Utilities.readProperties import ReadConfig

import os

class Test_001_Blogpost:

    baseURL = ReadConfig.getApplicationURL()
   

    # ----------------------------
    # Pytest fixture for setup/teardown
    # ----------------------------
    @pytest.fixture(autouse=True)
    def setup(self):
        # Open Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        # Close Chrome after test
        self.driver.quit()

    # ----------------------------
    # Random email generator
    # ----------------------------
    def random_email(self, size=8, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size)) + "@gmail.com"

    # ----------------------------
    # Test homepage title
    # ----------------------------
    def test_homepage_title(self):
       
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(2)
        print("Actual Title:", act_title)

        if act_title == "Automation Testing Practice":
           
            assert True
        else:
            # Take screenshot on failure
            screenshot_folder = ".\\Screenshots"
            os.makedirs(screenshot_folder, exist_ok=True)
            self.driver.save_screenshot(os.path.join(screenshot_folder, "homepage_title.png"))
            
            assert False

    # ----------------------------
    # Test filling blogpost form
    # ----------------------------
    def test_blogpost_form(self):
       
        self.driver.get(self.baseURL)
        blog = Practice(self.driver)

        # Fill the form
        blog.SetName("Arun")
        email = self.random_email()
        blog.Setemail(email)
        time.sleep(1)
        blog.SetPhone("1234567890")
        blog.SetAddress("#583, Some Street, City")
        blog.SetGender("Male")
        blog.Setcountry("Australia")
        time.sleep(1)
        blog.Clickcolor()
        blog.Selectpage()
        blog.Selectcheckbox()
        blog.Search("Test")
        blog.Searchbutton()
        time.sleep(2)

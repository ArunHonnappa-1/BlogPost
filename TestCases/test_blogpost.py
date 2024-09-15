import pytest
import time
from selenium import webdriver
from PageObjects.blogpost_practice import Practice
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
# from selenium.webdriver.common.by import By
import random
import string




class Test_001:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def homepage_title(self):
        self.logger.info("**** Test_001 blogpost page title*****")

        self.driver = webdriver.Chrome()

        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(3)
        print("act_title", act_title)
        # self.driver.close()

        if act_title == "Automation Testing Practice":
            assert True
            self.logger.info("*** Title***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "testhomepageTitle.png")
            assert False
            self.logger.info("***Title1*****")

        self.driver.close()


    def test_blogpost(self):
        self.logger.info("**** Blogpost details entry *****")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.logger.info("**** Chrome browser*****")

        self.driver.get(self.baseURL)
        self.blog = Practice(self.driver)

        self.blog.SetName("Arun")
        self.email = self.random_generator() + "@gmail.com"
        self.blog.Setemail(self.email)
        time.sleep(3)
        self.blog.SetPhone("123kejiwefnweh")
        self.blog.SetAddress("#583 xxx, xxx,xxx")
        self.blog.SetGender("Male")
        self.blog.Setcountry("Australia")
        time.sleep(3)
        self.blog.Clickcolor()
        self.blog.Selectpage()
        self.blog.Selectcheckbox()
        self.blog.Search("Test")
        self.blog.Searchbutton()
        time.sleep(3)
        self.logger.info("**** User entry to blogpost is completed *****")

    def random_generator(size=4, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for x in range(8))







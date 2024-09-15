from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Practice:
    namebox_id = "name"
    emailbox_id = "email"
    phonebox_id = "phone"
    addressbox_id = "textarea"
    rdbtnmale_id = "male"
    rdbtnfemale_id = "female"
    countrydropdown_id = "country"
    country_xpath = "(//option[@value='australia'])"
    colors_xpath = "(//option[@value='white'])"
    date_id = "datepicker"
    pagination_xpath = "(//a[@href='#'])[3]"
    checkbox_xpath = "(//input[@type='checkbox'])[12]"
    tab_id = "Wikipedia1_wikipedia-search-input"
    tabsearch_xpath = "(//input[@class='wikipedia-search-button'])"


    def __init__(self, driver):
        self.driver = driver

    def SetName(self, name):
        self.driver.find_element(By.ID, self.namebox_id).send_keys(name)

    def Setemail(self, email):
        self.driver.find_element(By.ID, self.emailbox_id).send_keys(email)


    def SetPhone(self, phone):
        self.driver.find_element(By.ID, self.phonebox_id).send_keys(phone)


    def SetAddress(self, address):
        self.driver.find_element(By.ID, self.addressbox_id).send_keys(address)

    def SetGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdbtnmale_id).click()

        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdbtnfemale_id).click()

        else:
            self.driver.find_element(By.ID, self.rdButtonMale_id).click()

    def Setcountry(self, value):
        drp = Select(self.driver.find_element(By.ID, self.countrydropdown_id))


        drp.select_by_visible_text(value)



    def Clickcolor(self):
        self.driver.find_element(By.XPATH, self.colors_xpath).click()

    def Selectpage(self):
        self.driver.find_element(By.XPATH, self.pagination_xpath).click()

    def Selectcheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath).click()

    def Search(self, text):
        self.driver.find_element(By.ID, self.tab_id).send_keys(text)

    def Searchbutton(self):
        self.driver.find_element(By.XPATH, self.tabsearch_xpath).click()







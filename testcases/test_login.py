import pytest
from selenium import webdriver
from pageobject.Loginpage import Login
from utilities.readproperties import Readconfig


class Test_001_Login:
    # baseurl = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

    baseurl=Readconfig.getApplicationURL()
    username=Readconfig.getUserEmail()
    password=Readconfig.getPassword()

    def test_homepageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        title = self.driver.title
        if title == "your store.Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            assert False

    def test_LoginPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(3)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Loginpage.png")
            self.driver.close()
            assert False



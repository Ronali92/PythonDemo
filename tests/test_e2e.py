import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckOutPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        #homePage.shopItem().click()
        #checkOutPage = CheckOutPage(self.driver)
        checkOutPage = homePage.shopItem()
        # //h4[@class='card-title']/a
        # //div[@class='card h-100']/div/h4
        # //div[@class='card h-100']/div/button
        mobiles = checkOutPage.getCardTitle()
        for mobile in mobiles:
            productname = mobile.find_element_by_xpath("div/h4/a").text
            if productname == "Blackberry":
                mobile.find_element_by_xpath("div/button").click()
                break
        # checkout = driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").text
        # if checkout == " Checkout ( 1 )"

        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_xpath(
            "//input[@class='validate filter-input form-control ng-untouched ng-pristine ng-valid']").send_keys("ind")
        self.presenceOfElement("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
        self.driver.get_screenshot_as_file("screen.png")
        # driver.find_element_by_name("name").send_keys("Ronali")
        # print(driver.find_element_by_name("name").get_attribute("value"))
        # driver.execute_script('return document.getElementsByName("name")[0].value')
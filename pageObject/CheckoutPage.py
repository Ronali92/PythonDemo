from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    name = (By.XPATH, "div/h4/a")
    cardFooter = (By.XPATH, "div/button")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
    #find_element_by_xpath("div/h4/a").text

    def getName(self):
        return self.driver.find_element(*CheckOutPage.name)

    #find_element_by_xpath("div/button")

    def getFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)
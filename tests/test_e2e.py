import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Page_objects.CheckOutPage import CheckOutPage
from Page_objects.FinalCheckout import CheckOutFinal
from Page_objects.HomeObjects import HomePage
from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        gotoShopButton = HomePage(self.driver)
        gotoShopButton.gotoShopPage().click()
        checkoutpage = CheckOutPage(self.driver)
        products = checkoutpage.getProdNames()
        for productNameList in products:
            productName = productNameList.find_element(By.XPATH, "div/h4/a").text
            if productName == "iphone X":
                productNameList.find_element(By.XPATH, "div/button").click()
        checkoutpage.CheckOutButton().click()
        checkOutfinal = CheckOutFinal(self.driver)
        checkOutfinal.clickCheckout().click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        alertText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in alertText




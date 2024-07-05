from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    prodList = (By.XPATH, "//div[@class='card h-100']")
    #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    checkoutbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getProdNames(self):
        return self.driver.find_elements(*CheckOutPage.prodList)


    def CheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutbutton)



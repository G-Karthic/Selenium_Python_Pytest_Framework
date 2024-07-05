from selenium.webdriver.common.by import By


class CheckOutFinal:

    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    finalCheckout = (By.CSS_SELECTOR, ".btn-success")


    def clickCheckout(self):
        return self.driver.find_element(*CheckOutFinal.finalCheckout)

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    #driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click()
    clickShopButton = (By.XPATH, "//a[contains(@href, 'shop')]")

    def gotoShopPage(self):
        return self.driver.find_element(*HomePage.clickShopButton)


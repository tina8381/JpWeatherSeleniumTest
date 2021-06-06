from basepage import BasePage


class VolcanoPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.level5 = self.driver.find_element_by_id("level_keyword05")
        self.level4 = self.driver.find_element_by_id("level_keyword04")
        self.level3 = self.driver.find_element_by_id("level_keyword03")
        self.level2 = self.driver.find_element_by_id("level_keyword02")
        self.level1 = self.driver.find_element_by_id("level_keyword01")


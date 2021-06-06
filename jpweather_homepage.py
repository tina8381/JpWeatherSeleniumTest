from basepage import BasePage


class WeatherHomepage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.warn_icon = self.driver.find_element_by_id("indexmenu_warn_img")
        self.yoho_icon = self.driver.find_element_by_id("indexmenu_yoho_img")
        self.cyclone_icon = self.driver.find_element_by_id("indexmenu_cyclone_img")
        self.kiken01_icon = self.driver.find_element_by_id("indexmenu_kiken01_img")
        self.kiken02_icon = self.driver.find_element_by_id("indexmenu_kiken02_img")
        self.kiken03_icon = self.driver.find_element_by_id("indexmenu_kiken03_img")
        self.tsunami_icon = self.driver.find_element_by_id("indexmenu_tsunami_img")
        self.quake_icon = self.driver.find_element_by_id("indexmenu_quake_img")
        self.volcano_icon = self.driver.find_element_by_id("indexmenu_volcano_img")

        self.warn_text = self.driver.find_element_by_id("indexmenu_warn_text")
        self.yoho_text = self.driver.find_element_by_id("indexmenu_yoho_text")
        self.cyclone_text = self.driver.find_element_by_id("indexmenu_cyclone_text")
        self.kiken01_text = self.driver.find_element_by_id("indexmenu_kiken01_text")
        self.kiken02_text = self.driver.find_element_by_id("indexmenu_kiken02_text")
        self.kiken03_text = self.driver.find_element_by_id("indexmenu_kiken03_text")
        self.tsunami_text = self.driver.find_element_by_id("indexmenu_tsunami_text")
        self.quake_text = self.driver.find_element_by_id("indexmenu_quake_text")
        self.volcano_text = self.driver.find_element_by_id("indexmenu_volcano_text")

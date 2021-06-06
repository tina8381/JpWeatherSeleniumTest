import os
from selenium import webdriver
from jpweather_homepage import WeatherHomepage
from volcano_page import VolcanoPage


class TestJpWeather:
    lang = "jp"
    url = "https://www.data.jma.go.jp/multi/index.html?lang=" + lang

    def setup_class(self):
        chromedriver = "/Users/Tina/Documents/Tina/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

    def teardown_class(self):
        self.driver.quit()

    def test_homepage_tabs(self):
        self.driver.get("https://www.data.jma.go.jp/multi/index.html?lang=jp")
        weather_homepage = WeatherHomepage(self.driver)
        assert weather_homepage.warn_text.text == "気象警報・注意報"
        assert weather_homepage.yoho_text.text == "天気予報"
        assert weather_homepage.cyclone_text.text == "台風情報"
        assert weather_homepage.kiken01_text.text == "危険度分布 : 土砂災害"
        assert weather_homepage.kiken02_text.text == "危険度分布 : 浸水害"
        assert weather_homepage.kiken03_text.text == "危険度分布 : 洪水"
        assert weather_homepage.tsunami_text.text == "津波警報・注意報"
        assert weather_homepage.quake_text.text == "地震情報"
        assert weather_homepage.volcano_text.text == "噴火警報・予報"

    def test_volcano_warnings(self):
        self.driver.get(self.url)
        weather_homepage = WeatherHomepage(self.driver)
        weather_homepage.volcano_icon.click()
        volcano_page = VolcanoPage(self.driver)
        assert volcano_page.level5.text == "避難"
        assert volcano_page.level4.text == "避難準備"
        assert volcano_page.level3.text == "入山規制"
        assert volcano_page.level2.text == "火口周辺規制"
        assert volcano_page.level1.text == "活火山であることに留意"

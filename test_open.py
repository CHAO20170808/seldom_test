from seldom import TestCase

class SimpleTest(TestCase):
    browser = "chrome"  # 指定要使用的瀏覽器

    def test_open_google(self):
        self.open("https://www.google.com")
        self.assertIn("Google", self.driver.title)

class MyWebTests(TestCase):
    browser = "chrome"  # 同样需要指定浏览器
    base_url = "https://steakmyhome.com.tw/"

    def test_visit_homepage(self):
        self.open(self.base_url)
        self.assertTitle("我家牛排官方網站 – 吃牛排 到我家")

    def test_find_element(self):
        self.open(self.base_url)
        element = self.find_element(("id", "nm-mobile-menu"))

    def test_click_link(self):
        self.open(self.base_url)
        # 需要根據實際網頁結構修改定位器
        pass

    def test_click_latest_news_link(self):
        self.open(self.base_url)
        # 需要根據實際網頁結構修改定位器
        pass
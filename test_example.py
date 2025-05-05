import seldom
from seldom import Steps

class SteakMyHomeTest(seldom.TestCase):

    def test_visit_homepage(self):
        """Visit the homepage"""
        self.open("https://steakmyhome.com.tw/")
        self.assertTitle("我家牛排官方網站 – 吃牛排 到我家")  # Replace with the actual title

    def test_find_element(self):
        """Find an element"""
        self.open("https://steakmyhome.com.tw/")
        element = self.find_element(css="#nm-mobile-menu")  # Replace with a valid selector
        self.assertIsNotNone(element) # Check if element is found

    def test_click_link(self):
        """Click a link"""
        self.open("https://steakmyhome.com.tw/")
        self.click(css="a[href='/menu/']")  # Replace with the correct link selector
        self.assertIn("/menu/", self.get_current_url()) # Check if URL changed

    def test_click_latest_news_link(self):
        """Click the latest news link"""
        self.open("https://steakmyhome.com.tw/")
        self.click(css=".latest-news-link a")  # Replace with the correct selector
        self.assertIn("/news/", self.get_current_url())  # Check if URL contains "/news/"

if __name__ == '__main__':
    seldom.main(browser="chrome")
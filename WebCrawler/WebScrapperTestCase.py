
# Unit test on a function

import WebScrapper
from threading import Thread, Lock
import queue
import requests
from bs4 import BeautifulSoup
import unittest


class WebScrapperTest(unittest.TestCase):

    def setUp(self):
        self.q = queue.Queue()
        self.f = open("logs1.txt", "w")
        self.w = WebScrapper.WebScrapper(self.q,{},self.f)
        self.urls = ["http://blog.simplesite.com/",
        "http://career.simplesite.com/",
        "http://blog.simplesite.com/",
        "http://career.simplesite.com/",
        "https://www.facebook.com/SimpleSite",
        "https://www.youtube.com/channel/UCilTiEWPXKl1OQaxq6yRj2g",
        "https://twitter.com/SimpleSiteHQ",
        "https://www.linkedin.com/company/1868558/",
        "http://career.simplesite.com",
        "http://blog.simplesite.com/",
        "http://career.simplesite.com",
        "http://blog.simplesite.com/"]

    
    def test_get_url(self):
        """
        Checking if urls are parsed correctly given a base url
        """
        result=self.w.parseUrls(requests.get("https://www.simplesite.com/"))
        print(result)
        self.assertEqual(self.urls,result)


    def tearDown(self):
        self.f.close()


if __name__ == '__main__':
    unittest.main()




# Importing required libraries

from threading import Thread, Lock
from queue import Queue
import requests
from bs4 import BeautifulSoup

lock = Lock()

class WebScrapper(Thread):
    """
    Webscrapper class executes recursive url scrapping concurrently
    """

    def __init__(self, queue, visitedUrlDict , file):
        
        Thread.__init__(self)

        self.queue = queue

        self.file = file

        self.visitedUrlDict = visitedUrlDict  # A dictionary to keep track of already visited urls

    
    def run(self):
        
        while True:
            
            url = self.queue.get()

            self.visitedUrlDict[url] = True
            
            try:
                content = self.getContent(url)
                parsedUrl = self.parseUrls(content)
                self.writeURL(url,parsedUrl)
                
            finally:
                self.queue.task_done()
    
    
    def getContent(self,url):

        """
        Given a url, fetches website content 
        """

        try:
            content = requests.get(url) 
            return content

        except Exception as e:
            pass
        
        
    def parseUrls(self,content):
        
        """
        Parses webpage content and returns a list of urls

        """
        try:
            text = BeautifulSoup(content.text, features="lxml")
            urls = []

            for a in text.find_all('a', href=True):
                if a["href"].startswith("http"):
                    urls.append(str(a["href"]))
                    if a["href"] not in self.visitedUrlDict:
                        self.queue.put(a["href"])

            return urls
        
        except Exception as e:
            pass
    
    
    
    def writeURL(self,url,parsedUrls):
        """
        A synchronised function to write parsed urls to file
        """
        lock.acquire()
        
        self.file.write(url + "\n")
        
        try:
            
            for link in parsedUrls:
                self.file.write("\t" + link +"\n")
            
        except Exception as e:
            pass

        lock.release()

        
def main():
    
    # Checks for valid input and initiates multithreading
    try: 
        link = input("Enter the base website to begin crawling: ")
        print(" Crawling in progress and the urls are being logged to logs.txt. Press Ctrl + C to stop.")
        r = requests.get(link)
        
        # Logfile to store urls
        f = open("logs"+".txt", "w")
        
        queue = Queue()
        visitedUrlDict = {}
        
        for x in range(5):
            worker = WebScrapper(queue,visitedUrlDict,f)
            worker.daemon = True
            worker.start()
       
        queue.put(link)
        queue.join()
        f.close()
        
    except Exception as e:
        print("Please provide a valid URL")
    

if __name__ == '__main__':
    main()

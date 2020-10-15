# WebCrawler

A simple multi-threaded python web crawler. The webcrawler is given a base url as input. It reads the content of url and identify other urls in the page and recursively visits each url and perfoms the same operations.

# MacOS Instruction

# Required Python Modules for the application:
- requests
 -bs4

# Install other dependencies using pip	
pip3 intall requests
pip3 install beautifulsoup4

# Running the Application

From the application directory, run the following command:

python3 WebScrapper.py

Enter the url when prompted.

The output will be printed to the log file named "logs.txt" until a keyboard interrupt is prompted.

# Running the test case file

From the application directory, run the following command:

python3 -m unittest WebScrapperTest.py

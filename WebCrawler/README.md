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

The ouput will be printed to the log file named "logs.txt" until a keyboard interrupt is prompted.

# Running the test case file

From the application directory, run the following command:

python3 -m unittest WebScrapperTest.py

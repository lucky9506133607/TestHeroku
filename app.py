from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from os import environ
import os
def Test():
	op = webdriver.ChromeOptions()
	op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	op.add_argument("--headless")
	op.add_argument("--no-sandbox")
	op.add_argument("--disable-dev-sh-usage")
	try:
	    print('in try block')
	    driver = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")), options=op)
	except Exception as e:
	    print("Exception arrived", e)
	driver.get("https://venetablinds.com.au/")
	print("Add options")
	print(driver.title)
	driver.quit()

if __name__ == "__main__":
	Test()
	print("Printed immediately.")
	time.sleep(20)
	print("Print after 20 seconds")
		
		

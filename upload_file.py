from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')

driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/FileUpload.html")

upload_input = driver.find_element_by_id("myFile")
path = os.path.abspath("upload.txt")

driver.save_screenshot("screenshots/before_upload.png")
upload_input.send_keys(path)
driver.save_screenshot("screenshots/after_upload.png")
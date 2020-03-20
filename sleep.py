from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')

driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/Waits.html")

driver.find_element_by_id("clickOnMe").click()
time.sleep(5)
print(driver.find_element_by_tag_name("p").text)

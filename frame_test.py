from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')

driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/iFrameTest.html")

print(driver.find_element_by_tag_name("h1").text)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
print(driver.find_element_by_tag_name("h1").text)
driver.switch_to.default_content()

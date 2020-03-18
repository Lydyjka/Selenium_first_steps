from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')

driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/Test.html")

driver.execute_script("arguments[0].click();", driver.find_element_by_id("newPage"))

value = "Lydyjka"



driver.execute_script("arguments[0].setAttribute('value', '" + value + "')", driver.find_element_by_id("fname"))

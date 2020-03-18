from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')

driver.get("https://www.w3schools.com/")

element = driver.find_element_by_id("navbtn_tutorials")

webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
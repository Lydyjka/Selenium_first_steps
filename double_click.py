from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')

driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/DoubleClick.html")

button = driver.find_element_by_id("bottom")

# webdriver.ActionChains(driver).double_click(button).perform()

webdriver.ActionChains(driver).context_click(button).perform()
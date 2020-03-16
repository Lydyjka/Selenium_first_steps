from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')
#driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
driver.maximize_window()

#cwiczenie: Single Input Field
#driver.find_element_by_class_name("form-control").send_keys("test")
#driver.find_element_by_xpath("//button[text()='Show Message']").click()

#cwiczenie: Two Input Fields
#driver.find_element_by_id("sum1").send_keys("5")
#driver.find_element_by_id("sum2").send_keys("3")
#driver.find_element_by_xpath("//button[text()='Get Total']").click()
#print(driver.find_element_by_xpath("//*[contains(@id,'displayvalue')]").text)
#print(driver.find_element_by_id("displayvalue").text)

#cwiczenie: Select List Demo
auto_select = Select(driver.find_element_by_id("select-demo"))
auto_select.select_by_visible_text("Monday")
print(driver.find_element_by_class_name("selected-value").text)

#cwiczenie: Multi Select List Demo
auto_select2 = Select(driver.find_element_by_id("multi-select"))
auto_select2.select_by_value("California")
auto_select2.select_by_value("Ohio")
auto_select2.select_by_value("Florida")
driver.find_element_by_id("printMe").click()
driver.find_element_by_id("printAll").click()  #probably there is a bug because the second element is displaying
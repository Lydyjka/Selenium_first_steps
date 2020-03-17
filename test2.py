from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')
#driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
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
#auto_select = Select(driver.find_element_by_id("select-demo"))
#auto_select.select_by_visible_text("Monday")
#print(driver.find_element_by_class_name("selected-value").text)

#cwiczenie: Multi Select List Demo
#auto_select2 = Select(driver.find_element_by_id("multi-select"))
#auto_select2.select_by_value("California")
#auto_select2.select_by_value("Ohio")
#auto_select2.select_by_value("Florida")
#driver.find_element_by_id("printMe").click()
#driver.find_element_by_id("printAll").click()  #probably there is a bug because the second element is displaying

#cwiczenie: Checkbox Demo
#driver.find_element_by_id("isAgeSelected").click()

#cwiczenie:Multiple Chexbox Demo
#driver.find_element_by_xpath("//label[text()='Option 1']//input[@type='checkbox']").click()
#driver.find_element_by_xpath("//label[text()='Option 2']//input[@type='checkbox']").click()
#driver.find_element_by_id("check1").click()

#cwiczenie: Radio Button Demo
driver.find_element_by_xpath("//*[@name='optradio' and @value='Male']").click()
driver.find_element_by_id("buttoncheck").click()
driver.find_element_by_xpath("//*[@name='optradio' and @value='Female']").click()
driver.find_element_by_id("buttoncheck").click()

#cwiczenie: Group Radio Buttons Demo
driver.find_element_by_xpath("//*[@name='gender' and @value='Male']").click()
driver.find_element_by_xpath("//*[text()='5 to 15']//input[@type='radio']").click()
driver.find_element_by_xpath("//button[text()='Get values']").click()

driver.find_element_by_xpath("//*[@name='gender' and @value='Female']").click()
driver.find_element_by_xpath("//*[text()='0 to 5']//input[@type='radio']").click()
driver.find_element_by_xpath("//button[text()='Get values']").click()
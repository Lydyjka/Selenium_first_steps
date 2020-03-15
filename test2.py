from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.maximize_window()


#cwiczenie: Single Input Field
#driver.find_element_by_class_name("form-control").send_keys("test")
#driver.find_element_by_xpath("//button[text()='Show Message']").click()

#cwiczenie: Two Input Fields
driver.find_element_by_id("sum1").send_keys("5")
driver.find_element_by_id("sum2").send_keys("3")
driver.find_element_by_xpath("//button[text()='Get Total']").click()
#print(driver.find_element_by_xpath("//*[contains(@id,'displayvalue')]").text)
print(driver.find_element_by_id("displayvalue").text)

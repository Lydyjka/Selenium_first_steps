from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/Test.html")
driver.maximize_window()
#driver.find_element_by_id("newPage").click()
#driver.close(_) #zamyka wszystkie okna na których był focus
#driver.quit() #zamyka wszystkie okna
#driver.find_element_by_id("fname")
#driver.find_element(By.ID, "fname") #inny sposób lokalizowania za pomoca id
#driver. find_element_by_id("clickOnMe")
#driver.find_element_by_name("fname")
#driver.find_element_by_link_text("Visit W3Schools.com!")
#driver.find_element_by_partial_link_text("W3Schools.com")
#driver.find_element_by_class_name("topSecret") #znajduje element nawet gdy klasa ma kilka nazw
#driver.find_element_by_tag_name("a")
#driver.find_element_by_tag_name("p")
#driver.find_element_by_tag_name("label") #pozwala grupować wyniki ale ciężko odnaleźć unikalny element"
#driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
#driver.find_element_by_xpath("//tbody//th")
#driver.find_element_by_xpath("//th")
#driver.find_element_by_xpath("//th[text()='Month']")
#driver.find_element_by_xpath("//button[@id='clickOnMe']")
#driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table")
driver. find_element_by_id("clickOnMe").click()
driver.switch_to.alert.accept()
driver. find_element_by_id("clickOnMe").click()
driver.switch_to.alert.dismiss()




















#driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
#driver.maximize_window()
#driver.find_element_by_id("newPage").click()
#driver.find_element_by_id("clickOnMe").click()
#driver.switch_to.alert.dismiss()
##driver.switch_to.alert.dismiss()
#driver.switch_to.alert.dismiss()
#auto_select = Select(driver.find_element_by_tag_name("select"))
#auto_select.select_by_visible_text("Volvo")
#auto_select.select_by_visible_text("Audi")
#auto_select.select_by_visible_text("Saab")
#auto_select.select_by_index(1)
#driver.find_element_by_xpath("//input[@type='checkbox']").click()
#driver.find_element_by_xpath("//input[@value='male']").click()
#driver.quit()



#driver.find_element_by_class_name("form-control").send_keys("My message")
#driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button").click()
#driver.find_element_by_css_selector("button.btn:nth-child(2)").click()
#driver.find_element_by_css_selector("button[class=btn.btn-default]").click()
#driver.find_element_by_class_name("btn-default").click()

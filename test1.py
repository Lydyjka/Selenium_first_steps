from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/Test.html")
# driver.maximize_window()
# driver.find_element_by_id("newPage").click()
# driver.close(_) #zamyka wszystkie okna na których był focus
# driver.quit() #zamyka wszystkie okna
# driver.find_element_by_id("fname")
# driver.find_element(By.ID, "fname") # inny sposób lokalizowania za pomoca id
# driver. find_element_by_id("clickOnMe")
# driver.find_element_by_name("fname")
# driver.find_element_by_link_text("Visit W3Schools.com!")
# driver.find_element_by_partial_link_text("W3Schools.com")
# driver.find_element_by_class_name("topSecret") #znajduje element nawet gdy klasa ma kilka nazw
# driver.find_element_by_tag_name("a")
# driver.find_element_by_tag_name("p")
# driver.find_element_by_tag_name("label") # pozwala grupować wyniki ale ciężko odnaleźć unikalny element"
# driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
# driver.find_element_by_xpath("//tbody//th")
# driver.find_element_by_xpath("//th")
# driver.find_element_by_xpath("//th[text()='Month']")
# driver.find_element_by_xpath("//button[@id='clickOnMe']")
# driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table")
# driver. find_element_by_id("clickOnMe").click()
# driver.switch_to.alert.accept()
# driver. find_element_by_id("clickOnMe").click()
# driver.switch_to.alert.dismiss()
#
# driver.find_element_by_name("username").send_keys(Keys.BACK_SPACE)
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
#
# auto_select = Select(driver.find_element_by_tag_name("select"))
# auto_select.select_by_visible_text("Volvo")
# auto_select.select_by_value("saab")
# auto_select.select_by_index(0)

# driver.find_element_by_xpath("//input[@type='checkbox']").click()
# driver.find_element_by_xpath("//input[@value='male']").click()
# print(driver.find_element_by_xpath("//input[@value='male']").text)
# print(driver.find_element_by_tag_name("h1").text)
# print(driver.find_element_by_tag_name("p").get_attribute("textContent"))
# driver.find_element_by_id("fname").send_keys("Lydyjka")
# print("Element text: " + driver.find_element_by_id("fname").get_attribute("value"))
#
# print(driver.find_element_by_id("smileImage").size.get("height"))
# print(driver.find_element_by_id("smileImage").get_attribute("naturalHeight"))

# driver.find_element_by_id("newPage").click()
# print(driver.title)
#
# current_window_name = driver.current_window_handle
# all_windows = driver.window_handles
#
# for window in all_windows:
#     if window != current_window_name:
#         driver.switch_to.window(window)
#
# print(driver.title)
# driver.switch_to.window(current_window_name)
# print(driver.title)

username_input = driver.find_element_by_name("username")
username_input.clear()
username_input.send_keys("Lydyjka")

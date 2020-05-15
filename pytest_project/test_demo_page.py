import pytest
from selenium import webdriver


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path=r'C:\Users\Lydyjka\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("file:///C:/Users/Lydyjka/Desktop/selenium_kurs_udemy/Test.html")
    driver.maximize_window()
    yield
    driver.quit()


def test_method(test_setup):
    assert driver.title == "Strona testowa"
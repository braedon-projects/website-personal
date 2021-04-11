from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #must pip install webdriver_manager
from selenium.webdriver.common.keys import Keys
import time


def bmi(sweight,sheight):
    weight= driver.find_element_by_xpath(".//*[@id='InputW']")
    weight.send_keys(sweight)

    heigh= driver.find_element_by_xpath(".//*[@id='InputH']")
    heigh.send_keys(sheight)

    login = driver.find_element_by_xpath(".//*[@id='s']")
    login.click()


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://127.0.0.1:4321/getbmi")


timer=2

bmi("120","72")
time.sleep(timer)
bmi("180","72")
time.sleep(timer)
bmi("300","72")
time.sleep(timer)
bmi("215","73")
time.sleep(timer)
bmi("300","68")
time.sleep(timer)
bmi("300","80")



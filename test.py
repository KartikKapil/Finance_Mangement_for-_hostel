from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.wheelmax.com/')
time.sleep(4)

selectYear = Select(driver.find_element_by_id("icm-years-select"))
selectYear.select_by_value('2019')

time.sleep(2)

selectMakes = Select(driver.find_element_by_id("icm-makes-select"))
selectMakes.select_by_value('58')
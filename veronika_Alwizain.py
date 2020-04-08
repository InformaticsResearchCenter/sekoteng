
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.telkomsel.com/")
sleep(2)
driver.find_element_by_id("va-ui-show").click()
sleep(2)
driver.find_element_by_id('va-ui-username').send_keys("Alwi")
sleep(2)
driver.find_element_by_id('va-ui-submit-username').click()
sleep(2)
driver.find_element_by_id('va-ui-textInput').send_keys("Halloo")
sleep(2)
driver.find_element_by_xpath('//*[@id="va-ui-send"]/div').click()
sleep(2)

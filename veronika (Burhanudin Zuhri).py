from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.telkomsel.com/")
sleep(2)
driver.find_element_by_id('va-ui-show').click()
sleep(2)
driver.find_element_by_id('va-ui-username').send_keys("Burhan")
sleep(2)
driver.find_element_by_id('va-ui-submit-username').click()
sleep(2)
driver.find_element_by_id('va-ui-textInput').send_keys("Hai")
sleep(2)
driver.find_element_by_xpath('//*[@id="va-ui-send"]/div').click()
sleep(2)
driver.find_element_by_id('va-ui-textInput').send_keys("Mantap!!!")
sleep(2)
driver.find_element_by_xpath('//*[@id="va-ui-send"]/div').click()
sleep(2)
driver.find_element_by_id('va-ui-textInput').send_keys("Wkwkwkwk")
sleep(2)
driver.find_element_by_xpath('//*[@id="va-ui-send"]/div').click()
sleep(2)
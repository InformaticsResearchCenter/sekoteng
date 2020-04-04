
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/?hl=id")
sleep(2)
driver.find_element_by_name("username").send_keys("jhon@gmailcom")
sleep(2)
driver.find_element_by_name("password").send_keys("xxxxxx")
sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click
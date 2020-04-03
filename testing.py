from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

driver = webdriver.Chrome()
driver.get("http://siap.poltekpos.ac.id/siap/besan.depan.php")
sleep(2)
driver.find_element_by_name("user_name").send_keys("1194008")
sleep(2)
driver.find_element_by_name("user_pass").send_keys("mahasiswaku")
sleep(2)
driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]").click()
sleep(2)
driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[2]").click()
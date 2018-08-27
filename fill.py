import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("Chrome Driver Path")
driver.get("Google Form Url")

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input').send_keys("Kanka Ben Formu Doldurayım mı ?")

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div[2]').click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[5]/content')))
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[4]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/input').send_keys("Dolduruyorum Dikkat Et")
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div[2]/div/div[1]/div/div[1]/input').send_keys("Vermem Telefon")
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div[2]/div/div[1]/div/div[1]/input').send_keys("Nokia 3310")
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div[2]/div[1]/div[2]/textarea').send_keys("Metin2")
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div[2]/div/div/label/div/div[2]/div/span').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content/span').click()


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://selenium.dev')
pas1 = driver.find_element_by_id('gsc-iw-id1')
print("Elementul dupa id este:" + pas1)
pas2 = driver.find_element_by_name('submit')
print("Elementul dupa nume este:" + pas2)
pas3 = driver.find_element_by_class_name('selenium-backers')
print('pas3')
pas4 = driver.find_element_by_xpath("// section[@class='hero homepage']/h1[1]")

time.sleep(4)
driver.close()

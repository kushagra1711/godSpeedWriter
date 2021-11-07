import os,time
from selenium import webdriver
from bs4 import BeautifulSoup, element
import pyautogui

url='https://monkeytype.com/'
browser=webdriver.Chrome(executable_path='chromedriver')
browser.get(url)

ele_wrd=browser.find_element_by_id('words')
soup=BeautifulSoup(ele_wrd.get_attribute('innerHTML'),'html.parser')
words = soup.find_all('div','word')
text_block=' '.join(word.text for word in words)

pyautogui.moveTo(800,1000)
pyautogui.click()
pyautogui.click()

for i in text_block:
    pyautogui.write(i) 

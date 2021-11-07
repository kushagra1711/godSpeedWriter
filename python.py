import os
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

keep_going= True
while keep_going:
    try:
        pyautogui.moveTo(800,1000)
        pyautogui.click()
        pyautogui.click()
        pyautogui.write(text_block)

        old_text_block=text_block
        search_string=text_block[-10:]

        ele_wrd=browser.find_element_by_id('words')
        soup=BeautifulSoup(ele_wrd.get_attribute('innerHTML'),'html.parser')
        words = soup.find_all('div','word')
        text_block=" ".join(word.text for word in words)

        text_block = text_block[text_block.index(search_string)].replace(search_string,'')
    except:
        keep_going=False
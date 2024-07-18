from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

with open('test.html','r', encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'lxml', )
# element = driver.find_element(By.CLASS_NAME, 'BpkText_bpk-text--heading-4__Y2VlY')
# # element.click()  # Example interaction
#print(soup)
x = soup.find_all('span', class_='BpkText_bpk-text__ODgwN BpkText_bpk-text--heading-4__Y2VlY', limit=5)
#print(x)
for i in x:
    print(i.text)
#soup.find_all('span', class_='BpkText_bpk-text__ODgwN BpkText_bpk-text--heading-4__Y2VlY', limit=5)
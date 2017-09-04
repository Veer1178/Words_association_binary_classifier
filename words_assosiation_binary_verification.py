# written by ron weiner
# python 3.5

from contextlib import closing
from selenium.webdriver import Firefox,Chrome # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from difflib import SequenceMatcher

wordsfromreview=("beer","cake","wine","waiter","water","wine")
len1=len(wordsfromreview)
vecw1=[0]*len1
print("vector dimension is:")
print(vecw1)
familylist=("drinks","food","atmosphere","server","adjective")

revcnt = [0]*5
i=0
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)
driver = webdriver.Firefox(firefox_profile=profile, executable_path=r'c:\\windows\\system32\\geckodriver.exe')

for singleword in wordsfromreview:
     i=0
     for familyword in familylist:
          url="https://onelook.com/thesaurus/?s="+singleword+"&f_rt="+familyword
          driver.get(url)
          WebDriverWait(driver, timeout=10).until(
                   lambda x: x.find_element_by_id('zone1'))
          try:
               elementtext  = driver.find_element_by_id('zone1').find_element_by_xpath("//div[@resid='1']").text
               if str(elementtext)==str(familyword):
                    revcnt[i]=revcnt[i]+1

          except :
              pass

          i=i+1
          driver.delete_all_cookies()

driver.close()
print("words from review:")
print(wordsfromreview)
print("family list is:")
print(familylist)
print("final match is:")
print(revcnt)

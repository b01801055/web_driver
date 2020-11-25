# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:15:09 2020

@author: Ron
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = None

ytlink="https://www.youtube.com/watch?v=rfscVS0vtbw"

try:
    cpath = 'chromedriver.exe'
    driver = webdriver.Chrome(cpath)
    driver.get(ytlink)
    # how do we fix this next statement?
    time.sleep(5)
    cs_selector = "#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer"
    e = driver.find_element(By.CSS_SELECTOR,cs_selector)
    time.sleep(3)
    txt_views = print(e.text)

finally:
    if driver is not None:
        driver.quit()
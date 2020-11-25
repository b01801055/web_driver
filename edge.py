# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:35:15 2020

@author: Ron
"""

from selenium import webdriver

driverPath = 'D:\web_driver\msedgedriver.exe'
browser = webdriver.Edge(executable_path=driverPath)
print(type(browser))
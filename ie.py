# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:44:45 2020

@author: Ron
"""
from selenium import webdriver

driverPath = 'D:\web_driver\IEDriverServer.exe'
browser = webdriver.Ie(executable_path=driverPath)
print(type(browser))


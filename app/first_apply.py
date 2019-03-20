import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '760BBKR228X2'

desired_caps['app'] = PATH('E:\package\dev-sit.20190129121419.apk')
# 如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

# 启动app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.quit()
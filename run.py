import time
from selenium import webdriver
from common import Commone,BasePage
import logging
import os
import web.test_01_task_allocation,web.test_02_my_task,web.test_final_approve,web.test_contract_info
from HTMLTestRunner import HTMLTestReportCN
import unittest
import os,time
from datetime import datetime

if __name__ == '__main__':
    print('====AutoTest Start====')
    commone = Commone()

    test_dir = './web'
    test_report_dir = './report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*')
    now = datetime.now().strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '/'\
               + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestReportCN(stream=fp, title='KTP Test Report', description='Result')
    runner.run(discover)
    fp.close()

    new_report = commone.new_file(test_report_dir)
    print(new_report)

    commone.send_email(new_report)

    print('====AutoTest Over====')









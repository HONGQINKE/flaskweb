import time
from selenium import webdriver
from common import Commone,BasePage
import logging
import os
import web.test_task_allocation,web.test_my_task,web.test_final_approve,web.test_contract_info
from HTMLTestRunner import HTMLTestReportCN
import unittest
import os,time
from datetime import datetime

if __name__ == '__main__':
    print('====AutoTest Start====')

    # 定义浏览器及初始化信息
    logging.info('--初始化浏览器--')
    dr = webdriver.Chrome()
    logging.info('--浏览器初始化完成--')

    logging.info('--引用BasePage对象--')
    basePage = BasePage(dr)

    commone = Commone()

    # 初始化数据
    global id_number
    id_number = commone.get_config_values('info', 'id_number')

    # 保存运行日志
    commone.log()

    #登录
    logging.info('--开始登录--')
    basePage.login()
    logging.info('--登录结束--')

    # 点击Reviw
    logging.info('--开始点击Reviw模块--')
    basePage.sleep(5)
    basePage.click(['css', '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
    basePage.sleep(5)
    logging.info('--Reviw模块点击成功--')

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









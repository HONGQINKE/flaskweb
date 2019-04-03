import time
from selenium import webdriver
from common import Commone,BasePage
import logging
import os
import unittest


class task_allocation(unittest.TestCase):
    def setUp(self):
        # 定义浏览器及初始化信息
        self.dr = webdriver.Chrome()

        self.basePage = BasePage(self.dr)
        self.commone = Commone()
        # 初始化数据


        # 保存运行日志
        self.commone.log()
        self.basePage.login()
        # 点击Reviw
        self.basePage.sleep(5)
        self.basePage.click(['css',
                        '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
        self.basePage.sleep(5)

    def tearDown(self):
        # 关闭浏览器
        self.basePage.quit()


    def test_task_allocation(self):
        #初始化身份证数据
        #commone = Commone()
        id_number = self.commone.get_config_values('info', 'id_number')
        #点击Task Allocation
        self.basePage.click(['xpath','//*[@id="103$Menu"]/li[4]/a'])
        #输入身份证号码
        self.basePage.type(['id','idNum'],id_number)
        #点击查询
        time.sleep(5)
        self.basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary'])
        #点击任务分配
        time.sleep(5)
        self.basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-table-wrapper.tableGrid > div > div > div > div > div > table > tbody > tr > td:nth-child(13) > button'])
        #输入刘虹
        time.sleep(5)
        self.basePage.type(['id','name'],'liuhong')
        #查询刘虹
        self.basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-col-6 > button'])
        #选择刘虹
        time.sleep(5)
        self.basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > label > span > input'])
        #点击ok
        self.basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary'])
        #确认ok
        time.sleep(3)
        self.basePage.click(['css','body div.ant-modal-confirm .ant-modal-body button.ant-btn.ant-btn-primary'])
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()


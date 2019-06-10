import sys
sys.path.append('..')

import time
from selenium import webdriver
from common import Commone,BasePage
import logging
import unittest
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.options import Options




class task_allocation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 定义浏览器及初始化信息
        #cls.chrome_options = Options()
        #cls.chrome_options.add_argument('--headless')

        #cls.dr = webdriver.Chrome(chrome_options=cls.chrome_options)
        cls.dr = webdriver.Chrome()

        cls.basePage = BasePage(cls.dr)
        cls.commone = Commone()
        cls.id_number = cls.commone.get_config_values('info', 'id_number')

        # 保存运行日志
        cls.commone.log()
        cls.basePage.login()
        # 点击Reviw
        cls.basePage.sleep(5)
        cls.basePage.click(['css',
                            '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
        cls.basePage.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.basePage.quit()


    def test_01_task_allocation_success(self):
        #点击Task Allocation
        self.basePage.click(['xpath','//*[@id="103$Menu"]/li[4]/a'])
        logging.info('Task Allocation Module clicked successfully')
        #输入身份证号码
        self.basePage.type(['id','idNum'],self.id_number)
        logging.info('Input id_number successfully')
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
        #self.basePage.click(['css','body div.ant-modal-confirm .ant-modal-body button.ant-btn.ant-btn-primary'])



if __name__ == '__main__':
    unittest.main()


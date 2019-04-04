import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from common import Commone,BasePage
import logging
import unittest


class my_task(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 定义浏览器及初始化信息
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



    def test_02_my_task(self):
        # 点击My Task
        self.basePage.click(['xpath', '//*[@id="103$Menu"]/li[3]/a'])
        time.sleep(5)
        # 输入身份证号码
        self.basePage.type(['id', 'idNum'], self.id_number)
        time.sleep(5)
        # 点击查询
        self.basePage.click(['css',
                        '#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary'])
        # 点击申请记录详情
        time.sleep(5)
        self.basePage.click(['css',
                        '#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(1) > a'])
        # 反欺诈框输入结果
        self.basePage.type(['id', 'antiFraudResutl'], 'ok')
        # 滚动下拉到底部
        self.basePage.scoll('1000')
        time.sleep(3)

        # 反欺诈结果点击Save
        self.basePage.click(['css',
                        '#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.scrollForm > form > div.align-center > button.ant-btn.mtPercent.ant-btn-primary'])
        # 反欺诈点击Information Asset
        time.sleep(3)

        #点击Clear
        self.basePage.click(['xpath','//*[@id="idPhotoFit"]/label[1]/span[2]'])
        #点击Yes
        self.basePage.click(['css','#personPhotoFit > label:nth-child(1) > span:nth-child(2)'])
        #点击Pass
        self.basePage.click(['css','#kptCheckOnline > label:nth-child(1) > span:nth-child(2)'])
        #输入Region信息
        self.basePage.type(['id','religion'],'regionA')
        self.basePage.sleep(3)
        #输入婚姻状态
        logging.info('[My Task] --start to input married status info--')
        self.dr.find_element_by_css_selector('#maritalStatus > div > div > div').clear()
        self.basePage.click(['css','#maritalStatus > div > div > div'])
        WebDriverWait(self.dr, 30).until(lambda x: x.find_element_by_xpath('/html/body/div[4]').is_displayed())
        menu =self.dr.find_element_by_xpath('/html/body/div[4]').find_element_by_xpath("/html/body/div[4]//ul/li[2]")
        menu.click()
        logging.info('[My Task] married status info input successfully')
        #滚动下拉到底部
        self.basePage.scoll('1000')
        #选择身份证省市区
        self.basePage.click(['id','idProvince'])
        WebDriverWait(self.dr, 30).until(lambda x: x.find_element_by_xpath('/html/body/div[5]').is_displayed())
        menu =self.dr.find_element_by_xpath('/html/body/div[5]').find_element_by_xpath("/html/body/div[5]//ul[1]/li[1]")
        menu.click()
        menu = self.dr.find_element_by_xpath("/html/body/div[5]//ul[2]/li[1]")
        menu.click()
        menu = self.dr.find_element_by_xpath("/html/body/div[5]//ul[3]/li[1]")
        menu.click()
        #输入身份证详细地址
        self.basePage.type(['id','idAddress'],'Address Detail')

        # 提交保存
        js = "var q=document.documentElement.scrollTop=1000"
        self.dr.execute_script(js)
        self.basePage.submit(['css',
                         '#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.loanMeterial > form > div > div > div.ant-col-13 > div.align-center > button.ant-btn.mtPercent.ant-btn-primary > span'])

        # 滚动条上滑
        self.basePage.scoll('-1000')
        #Work information中点击保存
        self.basePage.submit(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.loanMeterial > form > div > div > div.ant-col-13 > div.align-center > button.ant-btn.mtPercent.ant-btn-primary'])
      # 下拉到底部
        self.basePage.scoll('10000')
        # 点击Normal
        self.basePage.sleep(5)
        self.basePage.click(['css', '#checkSelf > label:nth-child(2) > span:nth-child(2)'])
         #点击Normal
        self.basePage.click(['css', '#checkContact > label:nth-child(3) > span:nth-child(2)'])
        # 点击Normal
        self.basePage.click(['css', '#checkWork > label:nth-child(3) > span:nth-child(2)'])
        # 点击Approved
        self.basePage.click(['css', '#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.PhoneApproved > form > div.align-center.formArea > button.ant-btn.mtPercent.ant-btn-primary'])
        #点击Approve Code
        WebDriverWait(self.dr, 30).until(lambda x: x.find_element_by_id('noteCode').is_displayed())
        menu = self.dr.find_element_by_id('noteCode')
        menu.click()
        #选择Approve Code
        WebDriverWait(self.dr, 30).until(lambda x: x.find_element_by_xpath('/html/body/div[5]').is_displayed())
        time.sleep(5)
        menu =self.dr.find_element_by_xpath('/html/body/div[5]').find_element_by_xpath("/html/body/div[5]//div/div/div/ul/li[1]")
        menu.click()
        #点击ok
        time.sleep(5)
        self.basePage.click(['css','body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary'])
        #确认ok
        self.basePage.click(['css','body > div:nth-child(11) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary'])


if __name__ == '__main__':
    unittest.main()


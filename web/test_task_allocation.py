import time
from selenium import webdriver
from common import Commone,BasePage
import logging
import os



def task_allocation(basePage,id_number):

    #点击Task Allocation
    basePage.click(['xpath','//*[@id="103$Menu"]/li[4]/a'])
    #输入身份证号码
    basePage.type(['id','idNum'],id_number)

    #点击查询
    time.sleep(5)
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary'])
    #点击任务分配
    time.sleep(5)
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-table-wrapper.tableGrid > div > div > div > div > div > table > tbody > tr > td:nth-child(13) > button'])
    #输入刘虹
    time.sleep(5)
    basePage.type(['id','name'],'liuhong')
    #查询刘虹
    basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-col-6 > button'])
    #选择刘虹
    time.sleep(5)
    basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > label > span > input'])
    #点击ok
    basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary'])
    #确认ok
    time.sleep(3)
    basePage.click(['css','body div.ant-modal-confirm .ant-modal-body button.ant-btn.ant-btn-primary'])
    time.sleep(3)


if __name__ == '__main__':
    # 定义浏览器及初始化信息
    dr = webdriver.Chrome()
    commone = Commone()
    basePage = BasePage(dr)

    # 初始化数据
    id_number = commone.get_config_values('info', 'id_number')

    # 保存运行日志
    commone.log()
    basePage.login()
    # 点击Reviw
    basePage.sleep(5)
    basePage.click(['css', '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
    basePage.sleep(5)
    #任务分配
    task_allocation(basePage,id_number)
    #关闭浏览器
    basePage.quit()


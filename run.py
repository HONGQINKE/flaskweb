import time
from selenium import webdriver
from common import Commone,BasePage
import logging
import os
import web.test_task_allocation,web.test_my_task,web.test_final_approve,web.test_contract_info




if __name__ == '__main__':
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
    #任务分配
    web.test_task_allocation.task_allocation(basePage,id_number)
    #任务处理
    web.test_my_task.my_task(basePage,id_number,dr)
    #终审
    web.test_final_approve.final_approve(basePage,id_number)
    #确认放款
    web.test_contract_info.contract_info(basePage,id_number)
    #关闭浏览器
    basePage.quit()


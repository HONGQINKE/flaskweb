import time
from selenium import webdriver
from common import Commone,BasePage
#from web.test_task_allocation import task_allocation
import web.test_task_allocation,web.test_my_task



if __name__ == '__main__':
    # 定义浏览器及初始化信息
    dr = webdriver.Chrome()
    commone = Commone()
    basePage = BasePage(dr)

    # 初始化数据
    id_number = commone.get_config_values('info', 'id_number')

    # 保存运行日志
    commone.log()

    #登录
    basePage.login()
    # 点击Reviw
    basePage.sleep(5)
    basePage.click(['css', '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
    basePage.sleep(5)
    #任务分配
    web.test_task_allocation.task_allocation()
    #My Task处理

    #关闭浏览器
    basePage.quit()
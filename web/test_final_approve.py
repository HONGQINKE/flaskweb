from selenium import webdriver
from common import Commone,BasePage

# 定义浏览器及初始化信息
dr = webdriver.Chrome()
commone = Commone()
basePage = BasePage(dr)

#初始化数据
id_number = commone.get_config_values('info', 'id_number')

#保存运行日志
commone.log()
basePage.login()

def final_approve():
    #点击Final Reviw
    basePage.click(['css','#\31 03\24 Menu > li.ant-menu-item.ant-menu-item-selected > a'])
    #输入身份证号
    basePage.type(['id','idNum'],id_number)
    #点击查询





if __name__ == '__main__':
    # 点击Reviw
    basePage.sleep(5)
    basePage.click(['css',
                    '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
    basePage.sleep(5)
    # my task任务处理
    final_approve()
    # 关闭浏览器
    # basePage.quit()

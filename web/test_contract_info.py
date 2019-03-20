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

def contract_info():
    #点击Final Reviw
    basePage.click(['xpath','//*[@id="102$Menu"]/li[1]/a'])
    #输入身份证号
    basePage.sleep(5)
    basePage.type(['id','idNum'],id_number)
    #点击查询
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary'])
    #点击详情
    basePage.sleep(5)
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-table-wrapper.tableGrid > div > div > div > div > div > table > tbody > tr > td:nth-child(2) > a'])
    #点击确认放贷
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.align-center.btnArea > button.ant-btn.btn.ant-btn-primary'])


if __name__ == '__main__':
    # 点击Account
    basePage.sleep(5)
    basePage.click(['css',
                    '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(2) > div.ant-menu-submenu-title > span > span'])
    basePage.sleep(5)
    # fianl approve
    contract_info()
    # 关闭浏览器
    #basePage.quit()

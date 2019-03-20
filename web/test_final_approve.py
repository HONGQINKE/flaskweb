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
    basePage.click(['xpath','//*[@id="103$Menu"]/li[1]/a'])
    #输入身份证号
    basePage.sleep(5)
    basePage.type(['id','idNum'],id_number)
    #点击查询
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary'])
    #点击详情
    basePage.sleep(5)
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-table-wrapper.tableGrid > div > div > div > div > div > table > tbody > tr > td:nth-child(2) > a'])
    #点击Phone check
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div:nth-child(3) > span'])
    #下拉到底部
    basePage.scoll('10000')
    #点击Approved
    basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.PhoneApproved > form > div:nth-child(3) > button.ant-btn.mtPercent.ant-btn-primary'])
    #点击ok
    basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary'])
    #确认ok
    basePage.click(['css','body > div:nth-child(9) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary'])


if __name__ == '__main__':
    # 点击Reviw
    basePage.sleep(5)
    basePage.click(['css',
                    '#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
    basePage.sleep(5)
    # fianl approve
    final_approve()
    # 关闭浏览器
    basePage.quit()

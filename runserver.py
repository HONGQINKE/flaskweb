import time
from selenium import webdriver

from common import log,get_config_values,BasePage
import logging
import os

#初始化信息
global url, username, password, width, height
url = get_config_values('info', 'url')
username = get_config_values('info', 'username')
password = get_config_values('info', 'password')
id_number = get_config_values('info', 'id_number')
width = get_config_values('info', 'width')
height = get_config_values('info', 'height')
seconds = get_config_values('info', 'seconds')

#保存运行日志
log()

#登录系统
# 运行ChromeDriver打开浏览器
dr = webdriver.Chrome()
# 设置浏览器窗口
dr.set_window_size(1366, 768)
# 设置全局操作超时时间
dr.implicitly_wait(5)
# 打开网址
dr.get('http://sit-approve.qude369.com/#/user/login')
driver = BasePage(dr)
driver.type(['id','userName'],'liuhong')
driver.sleep(3)
driver.type(['id','password'],'123456.com')
driver.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > button'])


#点击Reviw
driver.sleep(3)
driver.click(['css','#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
#点击Task Allocation
driver.click(['xpath','//*[@id="103$Menu"]/li[4]/a'])
#输入身份证号码
driver.type(['id','idNum'],'4932105402797845')
'''

#点击查询
time.sleep(5)
driver.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary').click()
#点击任务分配
time.sleep(5)
driver.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-table-wrapper.tableGrid > div > div > div > div > div > table > tbody > tr > td:nth-child(13) > button').click()
#输入刘虹
time.sleep(5)
driver.find_element_by_id('name').send_keys()
#查询刘虹
driver.find_element_by_css_selector('body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-col-6 > button').click()
#选择刘虹
time.sleep(5)
driver.find_element_by_css_selector('body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > label > span > input').click()
#点击ok
driver.find_element_by_css_selector('body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary').click()
#确认ok
time.sleep(3)
driver.find_element_by_css_selector('body div.ant-modal-confirm .ant-modal-body button.ant-btn.ant-btn-primary').click()
time.sleep(3)

#击My Task
driver.find_element_by_xpath('//*[@id="103$Menu"]/li[3]/a').click()
#输入身份证号码
driver.find_element_by_id('idNum').send_keys('4932105402797845')
time.sleep(5)
#点击查询
driver.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary').click()
#点击申请记录详情
time.sleep(5)
driver.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(1) > a').click()
#反欺诈框输入结果
driver.find_element_by_id('antiFraudResutl').send_keys('ok')
#滚动下拉到底部
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
#反欺诈结果点击Save
driver.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.scrollForm > form > div.align-center > button.ant-btn.mtPercent.ant-btn-primary').click()
#反欺诈点击Information Asset
#driver.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab').click()
#点击Yes
time.sleep(3)
#driver.find_element_by_css_selector('.label.ant-radio-button-wrapper.ant-radio-button-wrapper-checked  .span.ant-radio-button.ant-radio-button-checked').click()
driver.find_element_by_xpath('//*[@id="idPhotoFit"]/label[1]/span[2]').click()
driver.find_element_by_css_selector('#personPhotoFit > label:nth-child(1) > span:nth-child(2)').click()
driver.find_element_by_css_selector('#kptCheckOnline > label:nth-child(1) > span:nth-child(2)').click()
driver.find_element_by_id('religion').send_keys('regionA')
#输入婚姻状态
time.sleep(5)
driver.find_element_by_css_selector('#maritalStatus > div > div > div').click()
time.sleep(5)
driver.find_element_by_css_selector('body div.ant-select-dropdown.ant-select-dropdown--single >div > ul > nth-child(1)').click()
#ul = driver.find_element_by_css_selector('body div.ant-select-dropdown.ant-select-dropdown--single.ant-select-dropdown-placement-bottomLeft.ant-select-dropdown-hidden >div > ul ')
#ul.find_element_by_css_selector(' li:nth-child(2)').click()
#选择居住地址
#滚动下拉到底部
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
#输入居住详细地址
driver.find_element_by_id('idAddress').send_keys('Address')
#点击保存
#点击Phone Check
driver.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab > span').click()
#关闭浏览器
driver.quit()

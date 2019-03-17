import os
import configparser
import logging
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

class Commone:

    #读取配置文件
    def get_config_values(self,section,option):
        rootDir = os.path.split(os.path.realpath(__file__))[0]
        configFilePath = os.path.join(rootDir, 'config.ini')
        config = configparser.ConfigParser()
        config.read(configFilePath)
        return config.get(section = section ,option = option)



    #保存日志
    def log(self):
        log_file = os.path.join(os.getcwd(), 'log/liveappapi.log')
        log_format = '[%(asctime)s][%(name)s][%(levelname)s][%(message)s]'
        logging.basicConfig(level=logging.DEBUG, format=log_format, filename=log_file, filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(log_format)
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

class BasePage:


    def __init__(self, driver):
        self.driver = driver

    def get_img(self):
        '''截图'''
        path = os.path.join(os.get_cwd(), 'screenshots/')  # 拼接截图保存路径
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 按格式获取当前时间
        screen_name = path + rq + '.png'  # 拼接截图文件名
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("截图保存成功")
        except BaseException:
            logging.error("截图失败", exc_info=1)

    def find_element(self, selector):
        '''定位元素'''
        by = selector[0]
        value = selector[1]
        element = None
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    logging.error('没有找到元素')
                logging.info('元素定位成功。定位方式：%s，使用的值%s：' % (by, value))
                return element
            except:
                logging.error("报错信息：", exc_info=1)
                self.get_img()  # 调用截图
        else:
            logging.error('输入的元素定位方式错误')

    def type(self, selector, value):
        '''输入内容'''
        element = self.find_element(selector)
        element.clear()
        logging.info('清空输入内容')
        try:
            element.send_keys(value)
            logging.info('输入的内容：%s' % value)
        except BaseException:
            logging.error('内容输入报错', exc_info=1)
            self.get_img()

    def click(self, selector):
        '''点击元素'''
        element = self.find_element(selector)
        try:
            element.click()
            logging.info('点击元素成功')
        except BaseException:
            logging.error('点击元素报错', exc_info=1)
            self.get_img()

    def sleep(self, secondes):
        '''强制暂停'''
        time.sleep(secondes)
        logging.info('暂停%d秒' % secondes)

    def get_title(self):
        '''获取title'''
        title = self.driver.title
        logging.info('当前窗口的title是:%s' % title)
        return title

    def quit(self):
        self.driver.quit()
        logging.info('关闭浏览器')


    def login(self):
        # 初始化登录信息
        global url, username, password, width, height
        commone = Commone()
        url = commone.get_config_values('info', 'url')
        username = commone.get_config_values('info', 'username')
        password = commone.get_config_values('info', 'password')
        width = commone.get_config_values('info', 'width')
        height = commone.get_config_values('info', 'height')
        seconds = commone.get_config_values('info', 'seconds')
        # 设置浏览器窗口
        self.driver.set_window_size(width, height)
        # 设置全局操作超时时间
        self.driver.implicitly_wait(seconds)
        # 打开网址
        self.driver.get('http://sit-approve.qude369.com/#/user/login')
        #driver = BasePage(dr)
        self.type(['id', 'userName'], 'liuhong')
        self.sleep(5)
        self.type(['id', 'password'], '123456.com')
        self.click(
            ['css', '#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > button'])

    def scoll(self):
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

    def get_options(self):
        #//*[@id="ba991463-a0fd-413c-ec23-dcfe36882bbf"]/ul
        #demo_div = self.driver.find_element_by_xpath("""/html/body""")
        #print(demo_div.get_attribute('innerHTML'))
        #print(self.driver.execute_script("return arguments", demo_div))
        js_vul = """
                 var body = document.getElementsByTagName('body')[0];
                 function getChildNodes(node) {
                    console.log(node.childNodes)
                    if (node.hasChildNodes() && node.nodeType == 1) {
                        for (var i = 0; i < node.childNodes.length; i++) {
                            console.log(childNodes[i])
                            #getChildNodes(node.childNodes[i])
                        }
                    }
                 }
                 getChildNodes(body)
                 """
    def button_drop(self):

        self.click(['css','#maritalStatus > div > div > div'])
        # 找到dropdown-menu父元素
        WebDriverWait(driver,3).until(lambda driver: driver.find_element_by_css_selector('body > div:nth-child(6) > div > div').is_displayed())
        menu = self.find_element(['text',"Unmarried"])
        elements.click()



if __name__ == '__main__':
    log()




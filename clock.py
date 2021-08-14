# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


SUCCESS = 0
NET_ERROR = 1
LOGIN_ERROR = 2
SUBMIT_ERROR = 3
INPUT_ERROR = 4
UNKNOWN_ERROR = 5
ERROR_STATE = {SUCCESS: '打卡成功', NET_ERROR: '网络错误', LOGIN_ERROR: '登陆失败', SUBMIT_ERROR: '提交失败',
               INPUT_ERROR: '输入错误', UNKNOWN_ERROR: '未知错误'}


def clock(url, config):
    try:
        try:
            opts = Options()
            opts.add_argument('--headless')
            opts.add_argument('--disable-gpu')
            opts.add_argument('--no-sandbox')
            user = config['user']
            pwd = config['pwd']
            driver = webdriver.Chrome(chrome_options=opts, executable_path='/usr/local/bin/chromedriver')
            driver.get(url)
        except Exception as err:
            return NET_ERROR, str(err)
        try:
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("username").send_keys(user)
            driver.find_element_by_id("password").send_keys(pwd)
            driver.find_element_by_id("dl").click()
        except Exception as err:
            return LOGIN_ERROR, str(err)
        clock_info = config['clock_info']
        for name, opt in clock_info.items():
            if isinstance(opt, bool):
                if opt is True:
                    try:
                        button = driver.find_element_by_xpath(f"//div[@name='{name}' and @class='radio']")
                    except Exception as e:
                        pass
                    else:
                        button.click()
            elif isinstance(opt, int):
                try:
                    select = driver.find_element_by_xpath(f"//div[@name='{name}' and @class='radio']/div/div[{opt}]/span")
                except Exception as e:
                    pass
                else:
                    select.click()
            elif isinstance(opt, str):
                try:
                    area = driver.find_element_by_xpath(f"//div[@name='{name}' and @class='text']/input")
                except Exception as e:
                    pass
                else:
                    driver.execute_script('arguments[0].removeAttribute(\"readonly\")', area)
                    area.click()
                    area.clear()
                    time.sleep(20)
                    area.send_keys(opt)
                    time.sleep(2)
            time.sleep(1)
        try:
            driver.find_element_by_xpath(f"//div[@class='footers']/a").click()
            time.sleep(3)
            driver.find_element_by_xpath(f"//div[@id='wapcf']/div/div[2]/div[2]").click()
            time.sleep(3)
            driver.quit()
        except Exception as err:
            return SUBMIT_ERROR, str(err)
    except Exception as err:
        return UNKNOWN_ERROR, str(err)
    return SUCCESS, None


if __name__ == '__main__':
    print(clock('https://healthreport.zju.edu.cn/ncov/wap/default/index')[1])

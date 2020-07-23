from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, locator, timeout=30):
    """
        方法名：显式等待：查找元素
        参数：
            driver：手机的把柄
            locator:元素定位的反视
                格式：
                    - find_element_by_id: ("id", "value")
                    - find_element_by_xpath: ("xpath","value")
                    - find_element_by_accessbility_id：("aid","value")
                    - find_element_by_android_uiautomator: ("text", "Search")
            timeout: 超时时间，默认30秒
        返回值：
            - 找到了元素：返回元素
            - 没有找到元素：直接报错：timeout错误
    """
    if locator[0] == "aid":
        locator = ("accessibility id", locator[1]) # 把自定义的aid变成了原生支持的方式
    if locator[0] == "text":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))
    
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://132.232.44.158:9999/shopxo/")
driver.maximize_window() # 浏览器全屏

c = {'domain': '132.232.44.158', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'v5hosrtchbkfeu3qgldh744n80'}
driver.add_cookie(c)
driver.refresh()  # 刷新网页


# driver.find_element_by_link_text("登录").click()

# time.sleep(30)

# # 需要手动登录，登录完成打印cookie

# print(driver.get_cookies())
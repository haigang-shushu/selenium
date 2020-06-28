import time

from selenium import webdriver

# 自动化一个谷歌浏览器
# 一定要Chrome
# 如果没有配置驱动的环境变量，需要填写驱动的路径
# 用driver对象来控制浏览器，相当于控制浏览器的遥控器
driver = webdriver.Chrome()

# 打开百度网页
driver.get('https://www.baidu.com')

# 找到输入框，可以直接用ID 属性一次定位到目标元素
search_input = driver.find_element_by_id('kw')

# 操作目标元素，在输入框输入前端
search_input.send_keys('前端')

# 找到百度一下
baidu_btn = driver.find_element_by_id("su")

# 点击按钮
baidu_btn.click()

# 加延时看演示效果
time.sleep(3)

# 关闭浏览器
driver.quit()
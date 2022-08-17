from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
service = Service(executable_path="/Users/wuhaohao/test/chromedriver")
driver = webdriver.Chrome(service=service)

url="https://juejin.cn/post/7132490947320872974"

driver.get(url)

title = driver.title

content = driver.find_element(By.CLASS_NAME, "markdown-body")

fo = open(title + ".html", "w")

fo.write(content.get_attribute('outerHTML'))

driver.quit()

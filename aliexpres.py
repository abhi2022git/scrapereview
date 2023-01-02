from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.options import Options
myProxy = "20.210.26.214:3128"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': ''})
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=capabilities)  
driver.maximize_window()   
driver.get("https://feedback.aliexpress.com/display/productEvaluation.htm?v=2&productId=1005004231843512&ownerMemberId=2600662011&companyId=1100588726&memberType=seller&startValidDate=&i18n=true") 

#c = driver.find_element(By.XPATH,"//div[@id='root'] //div[@class='glodetail-wrap'] //div[@class='product-main'] //div[@class='product-main-wrap'] //div[@class='product-info'] //div[@class='product-reviewer'] //div[@class='overview-rating'] //div[@class='next-rating next-rating-large next-rating-grade-high']")
#customer_rating = c.find_element(By.XPATH,"//span[@class='overview-rating-average']")
#print(customer_rating.text)

page_title = driver.find_element(By.XPATH,"//div[@id='transction-feedback'] //div[@class='customer-reviews']")
print(page_title.text)

customer_name = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-user-info'] //span[@class='user-name'] //a")
review = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-main'] //div[@class='f-content'] //dl[@class='buyer-review'] //dt[@class='buyer-feedback'] //span")

for i in range(0,8):
    print(customer_name[i].text)
    print(review[i+i].text)

time.sleep(3)
driver.quit()  

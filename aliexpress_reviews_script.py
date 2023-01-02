from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import *
import csv

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
driver.get("https://feedback.aliexpress.com/display/productEvaluation.htm?v=2&productId=1005003712136270&ownerMemberId=239247290&companyId=246985295&memberType=seller&startValidDate=&i18n=true") 

csv_file = open("reviewdata.csv","a+",newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Id','Country','Customer Name','Rating','Review','Posted Date'])

product_id = driver.find_element(By.XPATH,"//form[@id='l-refresh-form'] //input[@id='productId']").get_attribute('value')
total_reviews =driver.find_element(By.XPATH,"//div[@id='transction-feedback'] //div[@class='customer-reviews']")
Review_count = total_reviews.text.strip('Customer Reviews (').strip(')')
customer_name = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-user-info'] //span[@class='user-name']")

customer_country = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-user-info'] //div[@class='user-country'] //b")

review = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-main'] //div[@class='f-content'] //dl[@class='buyer-review'] //dt[@class='buyer-feedback'] //span")
star = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-main'] //div[@class='f-rate-info'] //span[@class='star-view'] //span")
review_posted_date = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-main'] //div[@class='f-content'] //dl[@class='buyer-review'] //dt[@class='buyer-feedback'] //span[@class='r-time-new']")
List = []
for i in range(0,int(Review_count)):
    List.append([product_id,customer_country[i].text,customer_name[i].text,float(star[i].get_attribute('style').strip('width: ').strip('%;'))/20,review[i+i].text, review_posted_date[i].text])
for item in List:
    print(item)
    csv_writer.writerow(item)
csv_file.close()

time.sleep(3)
driver.quit()  

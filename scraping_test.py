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


csv_file = open("review.csv","w",newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Id','Country','Name','Rating','Review','Date'])

urls = ['https://feedback.aliexpress.com/display/productEvaluation.htm?v=2&productId=1005003712136270&ownerMemberId=239247290&companyId=246985295&memberType=seller&startValidDate=&i18n=true','https://feedback.aliexpress.com/display/productEvaluation.htm?v=2&productId=1005004231843512&ownerMemberId=2600662011&companyId=1100588726&memberType=seller&startValidDate=&i18n=true']

for url in urls:
    driver.get(url) 


    customer_name = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-user-info'] //span[@class='user-name']")
    customer_country = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-user-info'] //div[@class='user-country'] //b")
    review = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-main'] //div[@class='f-content'] //dl[@class='buyer-review'] //dt[@class='buyer-feedback'] //span")
    star = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-main'] //div[@class='f-rate-info'] //span[@class='star-view'] //span")
    product_id = driver.find_element(By.XPATH,"//form[@id='l-refresh-form'] //input[@id='productId']").get_attribute('value')

    review_posted_date = driver.find_elements(By.XPATH,"//div[@id='transction-feedback'] //div[@class='feedback-list-wrap'] //div[@class='feedback-item clearfix'] //div[@class='fb-main'] //div[@class='f-content'] //dl[@class='buyer-review'] //dt[@class='buyer-feedback'] //span[@class='r-time-new']")

    total_reviews =driver.find_element(By.XPATH,"//div[@id='transction-feedback'] //div[@class='customer-reviews']")
    Review_count = total_reviews.text.strip('Customer Reviews (').strip(')')


    List = []
    for i in range(0,int(Review_count)):
        List.append([product_id,customer_country[i].text,customer_name[i].text,int(star[i].get_attribute('style').strip('width: ').strip('%;'))/20,review[i+i].text, review_posted_date[i].text])
        #List.append(customer_name[i].text)
        #List.append(int(star[i].get_attribute('style').strip('width: ').strip('%;'))/20)
        #List.append(review[i+i].text)


    for item in List:
        print(item)
        csv_writer.writerow(item)

    #rating = driver.find_element(By.XPATH,"//div[@id='transction-feedback'] //div[@class='rate-detail util-clearfix'] //div[@class='rate-score'] //span[@class='rate-score-number'] //b")
    #rating_comp = driver.find_element(By.XPATH,"//div[@id='transction-feedback'] //div[@class='rate-detail util-clearfix'] //div[@class='rate-score'] //span[@class='rate-score-number'] //span")
    #print("overall rating :",rating.text,rating_comp.text )

    time.sleep(3)
csv_file.close()  
driver.quit()  

from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
driver.maximize_window()   
driver.get("https://www.amazon.com/Apple-MU8F2AM-A-Pencil-Generation/dp/B07K1WWBJK/ref=sr_1_1?qid=1672224803&refresh=1&s=electronics&sr=1-1") 


product_name = driver.find_element(By.XPATH,"//span[@id='productTitle']")
print(product_name.text)


product = driver.find_element(By.XPATH, "//div[@id='cm-cr-dp-review-list']")
title_name = product.find_element(By.XPATH,"//h3[@class='a-spacing-medium a-spacing-top-large']")
print(title_name.text)



customer = driver.find_element(By.XPATH,"//div[@id='customer_review-R11GYB0XGIZTM4']")
customer_n = customer.find_element(By.XPATH,"//div[@class='a-row a-spacing-mini']")
customer_name = customer_n.find_element(By.XPATH,"//a[@class='a-profile'] //div[@class='a-profile-content'] //span[@class='a-profile-name']")
print(customer_name.text)

rr = driver.find_element(By.XPATH,"//div[@id='customer_review-R11GYB0XGIZTM4']")
r = rr.find_element(By.XPATH,"//div[@class='a-row']")
ra = r.find_element(By.XPATH,"//a[@class='a-link-normal']")
rat = ra.find_element(By.XPATH,"//i[@class='a-icon a-icon-star a-star-5 review-rating']")
rating = rat.find_elements(By.XPATH,"//span[@class='a-icon-alt']")
print(rating[8].text)


des = driver.find_element(By.XPATH,"//div[@class='a-row a-spacing-small review-data']")
desc = des.find_element(By.XPATH,"//span[@class='a-size-base review-text']")
descr = desc.find_element(By.XPATH,"//div[@class='a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container']")
descri = descr.find_element(By.XPATH,"//div[@class='a-expander-content reviewText review-text-content a-expander-partial-collapse-content']//span")
print(descri.text)

time.sleep(3)
driver.quit()  

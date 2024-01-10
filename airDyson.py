
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yagmail
def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.dyson.com/hair-care/hair-stylers/airwrap")
    return driver
def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH,value='//*[@id="skip-navigation-target"]/div[2]/div[10]/div/div[3]/div/div/div/div/div/div[2]/div/div[8]/div/div[2]/div')
    return element.text
def onlyPrice(num):
    return float(num.replace('$',''))
price = main()
floatPrice = onlyPrice(price)
priceRightNow = [floatPrice]
print(priceRightNow)

sender = #enter email here
reciever = #enter email here

price = main()
floatPrice = onlyPrice(price)
priceRightNow.append(floatPrice)


subject = f" 'name here' ! The price for the air dyson today is ${floatPrice}. !"
contents = f"""
            Hey, 'name here' I just noticed the price is ${floatPrice}
            """
yag = yagmail.SMTP(user=sender, password='gmail password')
yag.send(to=reciever, subject=subject, contents=contents)


print("Email Sent!")


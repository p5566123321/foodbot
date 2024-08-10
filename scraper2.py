
from urllib.request import urlopen
from selenium import webdriver
import time

def scrapDelivery(location,store,choise):
#    driverPath = r"C:/chromedriver"  # r"C:/Users/Hatai/Desktop/chromedriver"
    driverPath = r"C:/Users/Hatai/Desktop/chromedriver"
    driver = webdriver.Chrome(driverPath)
    url = 'https://www.google.com.tw/'
    driver.get(url)
    #選擇外送商家
    if choise == 1:
        sell="Foodpanda"
    else:
        sell="Ubereat"

    #Google搜尋
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").clear()
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(location+"  "+store+"  "+sell)

    #Google好手氣
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]").click()

    #網址爬蟲

    time.sleep(3)
    re_url=driver.current_url
    if "foodpanda.com.tw" in re_url:
        return re_url
    elif "ubereats.com" in re_url:
        return re_url
    else:
        return "null"
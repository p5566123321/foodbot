from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
import re
import urllib.parse 

# 美食抽象類別
class Food(ABC):
 
    def __init__(self, area,category,page):
        self.area = area  # 地區
        self.category = category
        self.page=page 
 
    @abstractmethod
    def scrape(self):
        pass

def STR_to_NUM(data):
        line = tuple(data.split(','))
        num1 = float(line[1])
        num2 = float(line[2])
        line = [num1, num2]
        return line

addr=[""]


# 愛食記爬蟲
class IFoodie(Food):
    
    def scrape(self):
        

        num_data=self.area
        
        if (self.category):
            url= (
                "https://ifoodie.tw/explore/list/"+self.category+"?place=current&latlng="+str(num_data[0])+","+str(+num_data[1])+"&sortby=distance")
        else:
            url=(
                "https://ifoodie.tw/explore/list?place=current&latlng="+str(num_data[0])+","+str(+num_data[1])+"&sortby=distance")
        if self.page > 1:
            response = requests.get(url+"&page="+str(self.page))
        else:
            response = requests.get(url)
        
        soup = BeautifulSoup(response.content, "html.parser")
        

        # 爬取前十筆餐廳卡片資料
        cards = soup.find_all(
            'div', {'class': 'jsx-2133253768 restaurant-item track-impression-ga'},limit=10)
        i=1
        j=0
        #content = ""
        content = [["","","","","",""]]
        
        for card in cards:
            if j==4:
                j=0
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-2133253768 title-text"}).getText()
 
            stars = card.find(  # 餐廳評價
                "div", {"class": "jsx-1207467136 text"}).getText()
 
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-2133253768 address-row"}).getText()
            html="https://maps.googleapis.com/maps/api/distancematrix/xml?origins="+str(num_data[0])+","+str(+num_data[1])+"&destinations="+urllib.parse.quote(address)+"&key=AIzaSyCDrKaJjU6vbbvAl8sZL0zubzR-QCRuFZY"
            
            soup2=BeautifulSoup(requests.get(html).text, "html.parser")
            #tmp=soup2.find("distance")
            dist = soup2.find("distance").find("text").text

            print(dist)
            if i<=2:
                picture = card.find("img", {"src": re.compile('https://./*')})
            else:
                picture = card.find("img", {"data-src": re.compile('https://./*')})
            link = card.find(
                "a",{"class": "jsx-2133253768 click-tracker"})
            

            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            if i<=2:
                if i==1:
                    content[0][0]=f"{title}"
                    content[0][1]=f"{stars}顆星"
                    content[0][2]=f"{address}"
                    content[0][3]=f"{picture['src']}"
                    content[0][4]="https://ifoodie.tw"+f"{link['href']}"
                    content[0][5]=f"{dist}"
                else:
                    content=content+[[f"{title}",f"{stars}顆星",f"{address}",f"{picture['src']}","https://ifoodie.tw"+f"{link['href']}",f"{dist}"]]
                    #content += f"{title} \n{stars}顆星 \n{address} \n{picture['src']} \n\n"
            else:
                content=content+[[f"{title}",f"{stars}顆星",f"{address}",f"{picture['data-src']}","https://ifoodie.tw"+f"{link['href']}",f"{dist}"]]


                #content += f"{title} \n{stars}顆星 \n{address} \n{picture['data-src']} \n\n"
            
            j=0
            i=i+1

        return content

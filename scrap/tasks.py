import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from celery import shared_task

@shared_task
def New_Func():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome()
    driver.get('https://geonode.com/free-proxy-list')
    time.sleep(2)
    html_context = driver.page_source
    soup = BeautifulSoup(html_context,'html5lib')
    all_data=soup.find('tbody',attrs={'class':'bg-supportSecondary-200 font-roboto min-w-full'}).find_all('tr')
    data_list = []
    for data in all_data: 
        dic = {'ip_address':'','port':'','country':'','protocols':''}
        try:
            ip_address=data.find('td',attrs={'class':'py-2 md:py-3 px-4 whitespace-nowrap text-sm text-supportShamrock-base'}).span.string.strip()
            port = data.find_all('td', class_='text-supportShamrock-base')[1].span.string.strip()
            country =  data.find('td',attrs={'class':'py-2 md:py-3 px-4 whitespace-nowrap text-sm text-support1-base'}).title.string.strip()
            protocols = data.find('span',attrs={'class':'bg-support4-200 px-2 py-1 rounded uppercase'}).string
            
            dic['ip_address'] = ip_address
            dic['port']=port
            dic['country']=country
            dic['protocols'] = protocols
            data_list.append(dic)
        
        except:
            pass
    driver.close()
    import json
    json_data = json.dumps(data_list)
    if data_list:
        json_data = json.dumps(data_list)
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://127.0.0.1:8000/api/scrap/', data=json_data, headers=headers)
        print(response)
           
New_Func()
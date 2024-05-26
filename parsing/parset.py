import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agenet': "CrookedHands/2.0 (EVM x8), CurlyFingers20/1;p"}

def download(url):
    resp = requests.get(url, stream=True)
    image_name = url.split("/")[-1]
    r = open("C:\\Users\\user\\Desktop\\image\\" + image_name, 'wb')
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    for count in range(1, 8):
        
        url = f"https://scrapingclub.com/exercise/list_basic/%20page%201?page={count}"

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml") #html.parser

        data = soup.find_all('div', class_='w-full rounded border')

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url
            # print(card_url)
            # name = i.find("h4").text.replace('\n', '')
            # price = i.find("h5").text
            # url_img = "https://scrapingclub.com" + i.find("img", class_='card-img-top img-fluid').get('src')
            # print(name + '\n' + price + '\n'+ url_img + '\n')

def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(3) 
        soup = BeautifulSoup(response.text, "lxml")
        
        data = soup.find('div', class_='my-8 w-full rounded border')
        name = data.find('h3', class_="card-title").text
        price = data.find('h4').text
        text = data.find('p', class_='card-description').text
        url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top').get('src')
        download(url_img)
        yield name, price, text, url_img
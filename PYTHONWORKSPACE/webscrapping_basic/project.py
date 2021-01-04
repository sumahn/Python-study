import requests
from bs4 import BeautifulSoup
import time
# [오늘의 날씨]

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.status_code
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 날씨 언급 
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()

    # 현재, 최저, 최고 기온
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    
    # 오전/ 오후 강수확률
    morning_rain_rate = soup.find("span",attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span",attrs={"class":"point_time afternoon"}).get_text().strip()

    # 미세먼지, 초미세먼지
    # dust = soup.find("dl", attrs={"class":"indicator"}, text = ["미세먼지","초미세먼지"])
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()
    
    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    

def scrape_headline():
    try:
        print("[헤드라인 뉴스]")
        url = "http://news.naver.com"
        soup = create_soup(url)
        news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li")
        for index, news in enumerate(news_list):
             # title = news.div.a.get_text()
            title = news.find("a").get_text().strip()
            link = url + news.find("a")["href"]
            print(f"{index+1}. {title}")                
            print(f"(링크: {link})")
 
    except:
        print("Refused by server")
        time.sleep(5)
        


if __name__ == "__main__":
    # scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline()



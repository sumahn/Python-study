import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# headless chrome 설정
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
# options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

# url 접속
url = "http://daum.net"
browser = webdriver.Chrome("PYTHONWORKSPACE/webscrapping_basic/chromedriver.exe")
browser.maximize_window()
browser.get(url)

# 송파 헬리오시티 검색
browser.find_element_by_id("q").send_keys("송파 헬리오시티")
browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]').click()

# 데이터 가져오기
soup = BeautifulSoup(browser.page_source, 'lxml')
table = soup.find("tbody").find_all("tr")

# 출력 
for i, elems in enumerate(table):
    print("="*9, f"매물 {i+1}", "="*9)
    elem_list = elems.find_all("td")
    print(f"거래 :{elem_list[0].get_text()}")
    print(f"면적 :{elem_list[1].get_text()}")
    print(f"가격 :{elem_list[2].get_text()}")
    print(f"동 :{elem_list[3].get_text()}")
    print(f"층 :{elem_list[4].get_text()}")

browser.quit()


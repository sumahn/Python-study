# 패키지 
import requests
from bs4 import BeautifulSoup
import re
import csv

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# 웹 스크래핑 

teams = ["두산", "SK","키움","LG"]

for team in teams:

    with open("kbo_{}.csv".format(team), "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        title = "순 이름 팀 G 타석 타수 득점 안타 2타 3타 홈런 루타 타점 도루 도실 볼넷 사구 고4 삼진 병살 희타 희비 a 타율 c d e f g h j".split(' ')
        writer.writerow(title)

        for page in range(1, 3):
            print("현재 페이지는 {}페이지입니다.".format(page))
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
            url = "http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=0&ys=2020&ye=2020&se=0&te={0}&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn={1}".format(team, 30*(page-1))
            res = requests.get(url, headers = headers)
            soup = BeautifulSoup(res.content, "lxml")

            table = soup.find("table", attrs={"id":"mytable"})
            data_rows = table.find_all("tr")


            for row in data_rows:
                columns = row.find_all("td")
                if len(columns) <= 1 :
                    continue
                
                data = [col.get_text().strip() for col in columns]
                writer.writerow(data)

    print("-"*100)


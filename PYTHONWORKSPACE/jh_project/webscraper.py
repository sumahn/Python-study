import requests
from bs4 import BeautifulSoup
import csv 

class webscraper:
    def __init__(self, url, headers):
        self.url = url
        self.res = requests.get(self.url, headers)
        self.soup = BeautifulSoup(self.res.text, "lxml")

    def print_status(self):
        print(self.res.status_code)

    def get_data(self, filename, title, tag, rows, column):
        f = open(filename, "w", encoding="utf-8-sig", newline="")
        self.writer = csv.writer(f)
        self.title = title.split('\t')
        self.writer.writerow(self.title)

        self.data_rows = self.soup.find(tag).find_all(rows)
        
        for row in self.data_rows:
            columns = row.find_all(column)
            if len(columns) <=1: # 의미 없는 데이터 스킵
                continue
            data = [col.get_text().strip() for col in columns]
            self.writer.writerow(data) # 리스트 형태로 넣어주면 됨

        f.close()





                
                
    
    


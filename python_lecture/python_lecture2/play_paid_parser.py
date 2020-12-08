from bs4 import BeautifulSoup
import requests

# 가지고 오고자 하는 url 
url = "https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfcGFpZF9HQU1FEAcYAw%3D%3D:S:ANO1ljLtt38&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljJCqyI"
# response
res = requests.get(url)
# print(res.text, res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select("div.Ktdaqe  ")
# print(card_list) 
# card_list __str__을 지정해줬음 
# card_list는 array로 반환됨

print(">>>", card_list[0].get('class'))
for i in card_list:
    cards = i.select('div.uMConb ')  
    print(len(cards))
    for c in cards:
        title = c.select('div.WsMG1c')[0].text
        comp = c.select('div.KoLSrc')[0].text
        print("GAME NAME>>", title, "\n","GAME COMP>>", comp, "\n") 

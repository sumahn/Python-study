import requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # 올바로 코드를 가져왔다면 문제가 없고 그렇지 않으면 에러를 나게 하는 코드

# print("응답코드:",res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)
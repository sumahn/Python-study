# import Flask
from flask import Flask
import requests

# 객체 선언 
app = Flask(__name__)

# routing
@app.route("/google")
# crawling
def get_google():
    res = requests.get("http://www.google.com")
    return res.content

# 실행 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8081")

## 이렇게 접속하면 이미지 같은 거나 디자인이 안 불러와지는데 이거는 css 파일이 적용이 안 되기 때문임

    
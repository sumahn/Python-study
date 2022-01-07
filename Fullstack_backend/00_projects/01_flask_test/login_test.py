# import Flask, jsonify, request
from flask import Flask, jsonify, request, render_template

# 객체 선언 
app = Flask(__name__)


# routing 
@app.route('/login')
def login():
    # user_name, pw, email 이라는 parameter를 get 해라
    username = request.args.get('user_name')
    pw = request.args.get('pw')
    email = request.args.get('email')
    
    print(username, pw, email)
    # username이 회원가입한 유저인지 확인 
    if username == "suman":
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    
    # 프론트엔드로 리턴
    return return_data

# 정적 웹페이지 로드하기 
@app.route('/html_test')
def hello_html():
    return render_template('login.html')

# 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
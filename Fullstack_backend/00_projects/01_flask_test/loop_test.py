# import Flask, render_template 
from flask import Flask, render_template

# 객체 선언
app = Flask(__name__)

# routing
@app.route('/hello_loop')
def hello_name():
    value_list = ['list1','list2','list3']
    return render_template('loop.html', values = value_list)

# 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
    
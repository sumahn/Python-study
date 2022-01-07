from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=['GET'])
def test():
    # jsonify에 json data를 넣어도 되긴 함 
    return make_response(jsonify(success=True), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8082")

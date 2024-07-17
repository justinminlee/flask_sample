from flask import Flask, render_template

#Flask app initialization / 겍체 인스턴스 생성
app = Flask(__name__)


@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # Flask app을 debug mode로 실행
    # host 등을 직접 지정하고싶다면
    # app.run(host="127.0.0.1", port="5000", debug=True)
    
# 웹 페이지를 하나씩 추가할때마다 @app.route()를 추가하고 아래 함수를 작성해야함


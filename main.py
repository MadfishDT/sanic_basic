import sys # system 속성들을 사용하기 위한 import
from sanic import Sanic, response
from sanic.response import text, json

#sanic app을 생성한다.
app = Sanic('main')

#app route annotation으로 /(가장 처음 루트) 경로로 접근 하면, json을 리턴하는 함수를 생성한다.
@app.route('/')
async def test(request):
    return json({'hello': 'world'})

def main(argv):
    app.run(host='0.0.0.0', port=8000) # sanic app을 시작 한다. 호트르와 포트를 지정한다.

if __name__ == '__main__': #메인 Procedure if문
    main(sys.argv)
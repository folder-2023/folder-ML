from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, version='3.0', title='Folder API', description='Swagger 문서', doc="/api-docs")

test_api = api.namespace('test', description='조회 API')

@test_api.route('/')
class Test(Resource):
    def get():
        return 'Hello World!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
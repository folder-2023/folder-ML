from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import sentiment_prediction

app = Flask(__name__)
api = Api(app, version='3.0', title='Folder API', description='Swagger 문서', doc="/api-docs")

#test_api = api.namespace('test', description='조회 API')
prediction_api = api.namespace('prediction', description='감정분석 긍부정 API')


# @test_api.route('/STT2TTS')
# class Test(Resource):
#     def get(self):
#         return 'Hello World!'


@prediction_api.route('/predict', methods=['GET'])
class sentimentPredict(Resource):
    def get(self):
        if request.method == 'GET':
            text = request.args.get('text')
            predict = sentiment_prediction.Prediction()
            result = predict.text_prediction(text)
            return result


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)

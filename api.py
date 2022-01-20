from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from linear_reg_model import Linear_Reg_Model
import joblib
import pandas as pd
import sys

app = Flask(__name__)
api = Api(app)


class HomePage (Resource):
    def get(self):
        return 'Discovery Center Mission'


class RunModel (Resource):

    def post(self):
        model_status = "Failure"

        try:
            json_data = request.get_json(force=True)
            # print(json_data)
            loaded_model = joblib.load("linear_model_model.pkl")
            model = Linear_Reg_Model(loaded_model)
            results = model.predict(json_data)
            print(results)
            # model.run_model(model)
            model_status = "Success"

        except Exception as e:
            print((str(e)), file=sys.stderr)
        # finally:
        #     msg = self.writeResult(str(model_status))
        print(model_status)
        result = {'predictions': results.tolist()}
        return result


api.add_resource(HomePage, '/')
api.add_resource(RunModel, '/predict')


if __name__ == '__main__':
    app.run('0.0.0.0', '8888', debug=True)

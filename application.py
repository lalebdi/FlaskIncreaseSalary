from flask import Flask
from flask_restful import Api, Resource, reqparse

application = Flask(__name__)
app = application
api = Api(app)

post_args = reqparse.RequestParser()
post_args.add_argument("value", type=str, help="Value is required to proceed", required=True)
post_args.add_argument("mode", type=str, help="Choose between phone || name || amount", required=True)
post_args.add_argument("replace_with", type=str, help="Choose either --blank-- || --original--", required=True)


class IncreaseSalary(Resource):
    def get(self):
        return {"message": 'This URL will accept a PUT call with the following payload : '
                           '{"value": "<value goes here>", "mode": "phone || name || amount", "replace_with": "--blank-- || --original--"}'}

    def post(self):
        args = post_args.parse_args()
        output_data = processing_data(args)
        return output_data, 201


api.add_resource(IncreaseSalary, "/")
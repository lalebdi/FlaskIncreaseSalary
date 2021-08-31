from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

application = Flask(__name__)
app = application
api = Api(app)

put_args = reqparse.RequestParser()
put_args.add_argument("name", type=str, help="Name of employee is required", required=True)
put_args.add_argument("position", type=str, help="Position of employee")
put_args.add_argument("salary", type=int, help="How much they make? it is required", required=True)

employees = {"tony" : {"name" : "Tony Stark", "Position": "Ironman", "salary": 10000},
            "bruce": {"name" : "Bruce Wayne", "Position": "Batman", "salary": 20000},
            "jack": {"name" : "Jack Sparrow", "Position": "Pirate", "salary": 30000}}

def abort_if_employees_not_exist(name):
    if name not in employees:
        abort(404, message="Employee name does not exist")

class IncreaseSalary(Resource):
    def get(self, name):
        abort_if_employees_not_exist(name)
        return employees[name], 200

    def put(self, name):
        args = put_args.parse_args()
        employees[name] = args
        # output_data = processing_data(args)
        return employees[name], 201


api.add_resource(IncreaseSalary, "/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
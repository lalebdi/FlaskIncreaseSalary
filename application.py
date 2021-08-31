from flask import Flask
from flask_restful import Api, Resource, abort

application = Flask(__name__)
app = application
api = Api(app)

employees = {"tony": {"name": "Tony Stark", "salary": 10000},
             "bruce": {"name": "Bruce Wayne", "salary": 20000},
             "steve": {"name": "Steve Rogers", "salary": 20000.4},
             "jack": {"name": "Jack Sparrow", "salary": 30000}}


def abort_if_employees_not_exist(name):
    if name not in employees:
        abort(404, message="Employee name does not exist")


def process_increase_salary(profile):
    """ Takes a dict and increments the salary 5%"""
    initial_salary = employees[profile]["salary"]
    post_increase = initial_salary * 1.05
    post_increase = int(post_increase) if post_increase.is_integer() else float("{:.2f}".format(post_increase))
    employees[profile]["salary"] = post_increase


class IncreaseSalary(Resource):
    def get(self, name):
        abort_if_employees_not_exist(name)
        return employees[name], 200

    def put(self, name):
        abort_if_employees_not_exist(name)
        process_increase_salary(name)
        return employees[name], 201


class ShowEmployees(Resource):
    def get(self):
        return employees, 200

    def put(self):
        return {"message": "Select the employee you want to increase their salary"}, 404


api.add_resource(ShowEmployees, "/")
api.add_resource(IncreaseSalary, "/<string:name>")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=True)

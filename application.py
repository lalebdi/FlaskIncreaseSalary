from flask import Flask
from flask_restful import Api, Resource, abort

application = Flask(__name__)
app = application
api = Api(app)


employees = {"tony" : {"name" : "Tony Stark", "salary": 10000},
            "bruce": {"name" : "Bruce Wayne", "salary": 20000},
            "steve": {"name" : "Steve Rogers", "salary": 20000.4},
            "jack": {"name" : "Jack Sparrow", "salary": 30000}}

def abort_if_employees_not_exist(name):
    if name not in employees:
        abort(404, message="Employee name does not exist")


def process_increase_salary(profile):
    initial_salary = employees[profile]["salary"]
    PERCENT_INCREASE = 1.05
    post_increase = initial_salary * PERCENT_INCREASE
    if post_increase.is_integer():
        post_increase = int(post_increase)
    else:
        post_increase = "{:.2f}".format(post_increase)
    employees[profile]["salary"] = post_increase



class IncreaseSalary(Resource):
    def get(self, name):
        abort_if_employees_not_exist(name)
        return employees[name], 200

    def put(self, name):
        process_increase_salary(name)
        return employees[name], 201


api.add_resource(IncreaseSalary, "/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
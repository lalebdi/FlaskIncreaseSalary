import unittest
import requests

from application import app
# set the application to testing mode
app.testing = True


class TestApi(unittest.TestCase):
    BASE = "http://127.0.0.1:5000/"

    def test_get_everyone(self):
        expected = {"tony": {"name": "Tony Stark", "salary": 10000},
                    "bruce": {"name": "Bruce Wayne", "salary": 20000},
                    "steve": {"name": "Steve Rogers", "salary": 20000.4},
                    "jack": {"name": "Jack Sparrow", "salary": 30000}}
        res = requests.get(TestApi.BASE)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), expected)

    def test_no_param_get(self):
        expected = {"tony": {"name": "Tony Stark", "salary": 10000},
                    "bruce": {"name": "Bruce Wayne", "salary": 20000},
                    "steve": {"name": "Steve Rogers", "salary": 20000.4},
                    "jack": {"name": "Jack Sparrow", "salary": 30000}}
        res = requests.get(TestApi.BASE)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), expected)

    def test_tony_get(self):
        expected = {'name': 'Tony Stark', 'salary': 10000}
        res = requests.get(TestApi.BASE + 'tony')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), expected)

    def test_bruce_get(self):
        expected = {'name': 'Bruce Wayne', 'salary': 20000}
        res = requests.get(TestApi.BASE + 'bruce')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), expected)

    def test_steve_get(self):
        expected = {'name': 'Steve Rogers', 'salary': 20000.4}
        res = requests.get(TestApi.BASE + 'steve')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), expected)

    def test_jack_get(self):
        expected = {'name': 'Jack Sparrow', 'salary': 30000}
        res = requests.get(TestApi.BASE + 'jack')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), expected)

    def test_not_exist_get(self):
        expected = {'message': 'Employee name does not exist'}
        res = requests.get(TestApi.BASE + 'unknown')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json(), expected)

    def test_empty_get(self):
        expected = {'message': 'Employee name does not exist'}
        res = requests.get(TestApi.BASE + 'unknown')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json(), expected)

    def test_tony_put(self):
        expected = {'name': 'Tony Stark', 'salary': 10500}
        res = requests.put(TestApi.BASE + 'tony')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json(), expected)

    def test_bruce_put(self):
        expected = {'name': 'Bruce Wayne', 'salary': 21000}
        res = requests.put(TestApi.BASE + 'bruce')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json(), expected)

    def test_steve_put(self):
        expected = {'name': 'Steve Rogers', 'salary': 21000.42}
        res = requests.put(TestApi.BASE + 'steve')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json(), expected)

    def test_jack_put(self):
        expected = {'name': 'Jack Sparrow', 'salary': 31500}
        res = requests.put(TestApi.BASE + 'jack')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json(), expected)

    def test_not_exist_put(self):
        expected = {'message': 'Employee name does not exist'}
        res = requests.put(TestApi.BASE + 'unknown')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json(), expected)

    def test_empty_put(self):
        expected = {'message': 'Employee name does not exist'}
        res = requests.put(TestApi.BASE + 'unknown')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json(), expected)

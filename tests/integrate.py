'''simple integration tests to send requests to database'''
import requests
import unittest

URL = "http://localhost:5000/"

class IntegrationTests(unittest.TestCase):

    def test_post(self):
        r = requests.post(URL + "add", data = {'expression': '333+22+11+5'})
        self.assertEqual(r.status_code, 200)

    def test_post(self):
        r = requests.post(URL + "add", data = {'expression': '32-6+22/5'})
        self.assertEqual(r.status_code, 200)
      
    def test_post(self):
        '''invalid user input'''
        r = requests.post(URL + "add", data = {'expression': '32$6-'})
        # error 503 should be caught: the server is unable to handle the request
        self.assertEqual(r.status_code, 503)
      
if __name__ == '__main__':
    unittest.main()

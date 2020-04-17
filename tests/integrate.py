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
        # check if it is a server side error
        self.assertEqual('5', str(r.status_code)[0])
        
if __name__ == '__main__':
    unittest.main()

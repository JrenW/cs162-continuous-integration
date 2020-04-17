'''a simple integration test to send a request to the app server'''

import request
import unittest

class IntegrateTests(unittest.TestCase):

    def test_post(self):
        r = requests.post('http://localhost:5000/'+ “add”, data = {‘expression’: ‘3240532+3413+1000’})
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()


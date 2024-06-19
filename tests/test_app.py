import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_add_food(self):
        response = self.app.post('/add_food', data=dict(
            food='test_food',
            protein=10,
            amount=100
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test_food', response.data)

if __name__ == '__main__':
    unittest.main()

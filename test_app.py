import unittest
from flask import Flask
from flask_testing import TestCase
from your_flask_app_file import app

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hotel Booking', response.data)

if __name__ == '__main__':
    unittest.main()

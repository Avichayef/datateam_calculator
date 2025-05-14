"""
Calculator API Test:

1. Basic endpoint availability and health checks
2. Calculator operations functionality
3. Error handling and edge cases
4. Input validation
5. Web interface availability

Usage:
    python3 -m pytest tests/test_calculator.py
"""

import unittest
from app.main import app
import json

class TestCalculatorAPI(unittest.TestCase):
    """
    Test suite for the Calculator API.
        
    """

    def setUp(self):
        """
        Set up test client before each test.
        Creates a test client that can be used to make requests to the application.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_health_endpoint(self):
        """
        Test the health check endpoint.
        
        """
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'healthy')

    def test_api_info(self):
        """
        Test the API information endpoint.

        """
        response = self.app.get('/api')
        self.assertEqual(response.status_code, 200)
        self.assertIn('endpoints', response.json)
        self.assertIn('message', response.json)

    def test_home_page(self):
        """
        Test the home page (web interface).
        
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    def test_calculate_operations(self):
        """
        Test all calculator operations.
        
        """
        test_cases = [
            {'a': 10, 'b': 5, 'operation': '+', 'expected': 15},
            {'a': 10, 'b': 5, 'operation': '-', 'expected': 5},
            {'a': 10, 'b': 5, 'operation': '*', 'expected': 50},
            {'a': 10, 'b': 5, 'operation': '/', 'expected': 2},
        ]

        for test in test_cases:
            response = self.app.post('/calculate', 
                                   data=json.dumps({
                                       'a': test['a'],
                                       'b': test['b'],
                                       'operation': test['operation']
                                   }),
                                   content_type='application/json')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['result'], test['expected'])

    def test_invalid_numbers(self):
        """
        Test handling of invalid numeric inputs.

        """
        test_cases = [
            {'a': 'abc', 'b': 5, 'operation': '+'},
            {'a': 10, 'b': 'def', 'operation': '-'},
            {'a': None, 'b': 5, 'operation': '*'},
            {'a': 10, 'b': None, 'operation': '/'}
        ]

        for test in test_cases:
            response = self.app.post('/calculate',
                                   data=json.dumps(test),
                                   content_type='application/json')
            
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
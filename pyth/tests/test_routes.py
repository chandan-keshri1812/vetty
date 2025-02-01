
import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.valid_api_key = 'supersecretkey'  
        
    def test_get_coins_without_api_key(self):
        response = self.app.get('/crypto/coins')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid or missing API key', response.json['message'])

    def test_get_coins_with_valid_api_key(self):
        headers = {'X-API-KEY': self.valid_api_key}
        response = self.app.get('/crypto/coins', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_categories_without_api_key(self):
        response = self.app.get('/crypto/categories')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid or missing API key', response.json['message'])

    def test_get_categories_with_valid_api_key(self):
        headers = {'X-API-KEY': self.valid_api_key}
        response = self.app.get('/crypto/categories', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_coin_details_without_api_key(self):
        response = self.app.get('/crypto/coins/bitcoin')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid or missing API key', response.json['message'])

    def test_get_coin_details_with_valid_api_key(self):
        headers = {'X-API-KEY': self.valid_api_key}
        response = self.app.get('/crypto/coins/bitcoin', headers=headers)
        self.assertEqual(response.status_code, 200)
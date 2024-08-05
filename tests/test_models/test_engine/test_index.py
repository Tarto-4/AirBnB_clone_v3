#!/usr/bin/python3
"""
test_index.py
"""
import unittest
from flask import Flask, jsonify
from api.v1.app import app

class TestIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the Flask app"""
        cls.client = app.test_client()
        cls.client.testing = True

    def test_status(self):
        """Test the /status route"""
        response = self.client.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "OK"})

    def test_stats(self):
        """Test the /stats route"""
        response = self.client.get('/api/v1/stats')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        # Optionally, check if specific classes are present in the response
        self.assertIn("Amenity", response.json)
        self.assertIn("City", response.json)
        self.assertIn("Place", response.json)
        self.assertIn("Review", response.json)
        self.assertIn("State", response.json)
        self.assertIn("User", response.json)

if __name__ == '__main__':
    unittest.main()

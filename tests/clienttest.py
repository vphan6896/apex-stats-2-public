#!/usr/bin/python
import os

import unittest
import json
from .. import app.app
from unittest.mock import MagicMock

# mock impl from Johannes Fahrenkrug on Stack Overflow
# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)
    elif args[0] == 'https://api.github.com':
        return MockResponse({"class": "cloud"}, 200)
    return MockResponse(None, 404)


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_search(self):
	ret = app.search()
	val = ret['class']
	self.assertEqual(val, 'cloud')

if __name__ == '__main__':
    unittest.main()

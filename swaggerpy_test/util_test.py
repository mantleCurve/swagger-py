#!/usr/bin/env python3

#
# Copyright (c) 2013, Digium, Inc.
#

import unittest
from swaggerpy.swagger_model import json_load_url
from swaggerpy.http_client import SynchronousHttpClient


class UtilTest(unittest.TestCase):
    def test_json_load_url(self):
        # Test loading a local file
        client = SynchronousHttpClient()
        result = json_load_url(client, 'file:test-data/1.1/simple/resources.json')
        self.assertTrue(isinstance(result, dict))
        self.assertEqual('1.1', result['swaggerVersion'])


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
'''
Module: 'test_client'
'''

import client
from typing import Mapping, Sequence, Any, Dict
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test class'''
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        '''Test the org methed for a correct value'''
        # Create a GithubOrgClient instance with the org name
        org_client = GithubOrgClient(org_name)
        result = org_client.org
        expected_response = mock_get.return_value
        # Assert that the result matches the expected response
        self.assertEqual(result, expected_response)
        # Assert that get_json was called once with the expected URL
        mock_get.assert_called_once


if __name__ == '__main__':
    unittest.main()

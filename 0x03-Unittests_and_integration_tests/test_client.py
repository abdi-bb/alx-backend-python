#!/usr/bin/env python3
'''
Module: 'test_client'
'''

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
        org_client = GithubOrgClient(org_name)
        result = org_client.org
        expected_response = mock_get.return_value
        self.assertEqual(result, expected_response)
        mock_get.assert_called_once

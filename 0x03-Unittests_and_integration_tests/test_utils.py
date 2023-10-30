#!/usr/bin/env python3
'''
Module: 'test_utils.py'
'''

import unittest
from parameterized import parameterized
import utils
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock, MagicMock
import requests


class TestAccessNestedMap(unittest.TestCase):
    '''Class for testing utils.access_nested_map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_result: Any) -> None:
        '''Method to test that the method returns what it is supposed to.'''
        self.assertEqual(utils.access_nested_map(
            nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        '''Test whether the access_nested_map raises exception'''
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test the get_json function."""

    @parameterized.expand(
            [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch('utils.get_json')
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict,
                      mock_get) -> None:
        """Test that get_json returns the expected result."""
        mock_get.return_value = test_payload
        result = utils.get_json(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()

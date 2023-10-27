#!/usr/bin/env python3
'''
Module: 'test_utils.py'
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


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
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__':
    unittest.main()

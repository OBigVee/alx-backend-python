#!/usr/bin/env python3
"""parameterize unit tests """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """nested test class"""

    @parameterized.expand(
        [
            (
                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2),
            )
        ]
    )
    def test_access_nested_map(self, map, path, expected):
        """return excepted correct output"""
        output = access_nested_map(map, path)
        self.assertEqual(output, expected)

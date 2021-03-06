#!/usr/bin/env python3
"""parameterize unit tests """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """nested test class"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, map, path, expected):
        """return excepted correct output"""
        output = access_nested_map(map, path)
        self.assertEqual(output, expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(self, map, path, expected):
        """ """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)

            self.assertEqual(str(e.exception)[1:-1], expected)


class TestGetJson(unittest.TestCase):
    """json test result"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("test_utils.get_json")
    def test_get_json(self, test_url, test_payload, mock_get):
        """get_json test case"""
        mock_get.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """test memoize"""
    def test_memoize():
        """assert called once"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once

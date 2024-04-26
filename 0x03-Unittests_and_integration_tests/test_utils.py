#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ({"name": {"school": {"ALX": "SWE"}}},
             ("name", "school", "ALX"), "SWE")
            # ({"name":{"school":{"ALX":{"SWE"}}}}, (""))
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected_output (_type_): _description_
        """
        result = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(result, expected_output)

        @parameterized.expand(
            [({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)]
        )
        def test_access_nested_map_exception(self,
                                             nested_map,
                                             path,
                                             expected_output):
            """_summary_

            Args:
                nested_map (_type_): _description_
                path (_type_): _description_
                expected_output (_type_): _description_
            """
            with self.assertRaises(expected_output) as context:
                access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, expected_output):
        """_summary_

        Args:
            url (_type_): _description_
            expected_output (_type_): _description_
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch("requests.get", return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_memoize(self):
        """_summary_"""

        class TestClass:
            """_summary_"""

            def a_method(self):
                """_summary_"""
                return 42

            def a_property(self):
                """_summary_"""
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, "a_method") as mock_method:
            mock_method.return_value = 42

            result_1 = test_obj.a_property
            result_2 = test_obj.a_property

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
            mock_method.assert_called_once()

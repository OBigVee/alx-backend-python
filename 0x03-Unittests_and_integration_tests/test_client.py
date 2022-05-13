#!/usr/bin/env python3
""" """
import unittest

from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ """
    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload":True})
    def test_org(self, org_name, mock_get):
        """return value"""
        tClient = GithubOrgClient(org_name)
        return_test = test_client.org
        self.assertEqual(return_test, mock_get.return_value)
        mock_get.assert_called_once

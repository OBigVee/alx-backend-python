#!/usr/bin/env python3
"""Client Test"""
import unittest

from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """return value"""
        tClient = GithubOrgClient(org_name)
        return_test = test_client.org
        self.assertEqual(return_test, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """test _public_repos_url"""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value={"repos_url": "holberton"},
        ) as mock_get:
            json = {"repos_url": "holberton"}
            client = GithubOrgClient(json.get("repos_url"))
            return_test = client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(return_test, mock_get.return_value.get("repos_url"))

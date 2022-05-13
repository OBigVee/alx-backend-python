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
        """_public_repos_url"""
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

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """public_repos"""
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/",
        ) as mock_pub:
            client = GithubOrgClient("hoberton")
            return_result = client.public_repos()
            self.assertEqual(return_result, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected_return):
        """to has_license"""
        client = GithubOrgClient("holberton")
        return_result = client.has_license(repo, license_key)
        self.assertEqual(expected_return, return_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing"""

    @classmethod
    def setUpClass(cls):
        """Initialize"""
        cls.get_patcher = patch("requests.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """clean up"""
        cls.get_patcher.stop()

    def test_public_repos_url(self):
        """_public_repos_url"""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value={"repos_url": "holberton"},
        ) as mock_get:
            client = GithubOrgClient("holberton")
            return_result = client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(return_result, mock_get.return_value.get("repos_url"))

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected_return):
        """to has_license"""
        client = GithubOrgClient("holberton")
        return_result = client.has_license(repo, license_key)
        self.assertEqual(expected_return, return_result)

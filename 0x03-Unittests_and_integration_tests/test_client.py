#!/usr/bin/env python3
'''
Module: 'org_client'
'''

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """ Test clas """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """ Test that org method returns the correct value """
        org_client = GithubOrgClient(org_name)
        result = org_client.org
        self.assertEqual(result, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """ Test _public_repos_url mehod """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            org_client = GithubOrgClient(test_json.get("repos_url"))
            result = org_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(result,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """ Test public_repos method """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            org_client = GithubOrgClient("hoberton")
            result = org_client.public_repos()
            self.assertEqual(result, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """ Test has_license method """
        org_client = GithubOrgClient("holberton")
        result = org_client.has_license(repo, license_key)
        self.assertEqual(expected_return, result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test class """
    @classmethod
    def setUpClass(cls):
        """ SetUpClass for unittest """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ Stop test """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test public_repos mehod """
        test_class = GithubOrgClient("holberton")
        assert True

    def test_public_repos_with_license(self):
        """ Test public_repos method with the argument license """
        test_class = GithubOrgClient("holberton")
        assert True


if __name__ == '__main__':
    unittest.main()

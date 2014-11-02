import unittest

from github_api import GitHubSocialNetwork

class GitHubApiTests(unittest.TestCase):
    def setUp(self):
        self.github = GitHubSocialNetwork("Legena")

    def test_following(self):
        self.assertEqual(self.github.following(),
        ['RadoRado', 'Ivaylo-Bachvarov'])

    def test_is_following(self):
        self.assertTrue(self.github.is_following('RadoRado'))
        self.assertFalse(self.github.is_following('Pesho'))

if __name__ == '__main__':
    unittest.main()
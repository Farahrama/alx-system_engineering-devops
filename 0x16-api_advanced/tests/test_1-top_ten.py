import unittest
from 1-top_ten import top_ten

class TestTopTen(unittest.TestCase):

    def test_valid_subreddit(self):
        # Test with a valid subreddit name
        result = top_ten('programming')
        self.assertIsNotNone(result)  # Ensure it returns something

    def test_invalid_subreddit(self):
        # Test with an invalid subreddit name
        result = top_ten('this_is_a_fake_subreddit')
        self.assertEqual(result, None)  # Should return None for invalid subreddit

if __name__ == '__main__':
    unittest.main()

import unittest
import networking

class TestPostFetcher(unittest.TestCase):
    def test_something(self):
        title = networking.fetchPost()
        self.assertEqual(title, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit")

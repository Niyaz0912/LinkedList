import unittest
from QueueClass import CharQueue


class TestCharQueue(unittest.TestCase):
    def test_is_empty(self):
        queue = CharQueue(5)
        self.assertTrue(queue.is_empty())
        queue.enqueue('a')
        self.assertFalse(queue.is_empty())

    def test_is_full(self):
        queue = CharQueue(3)
        self.assertFalse(queue.is_full())
        queue.enqueue('a')
        queue.enqueue('b')
        queue.enqueue('c')
        self.assertTrue(queue.is_full())

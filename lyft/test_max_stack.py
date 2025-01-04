import unittest
from max_stack import Stack


class test_max_stack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_top(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.top(), 20, "Top should return the last pushed element")

    def test_push_and_get_max(self):
        self.stack.push(5)
        self.stack.push(15)
        self.stack.push(10)
        self.assertEqual(self.stack.get_max(), 15, "get_max should return the maximum value")

    def test_pop_updates_top_and_max(self):
        self.stack.push(3)
        self.stack.push(6)
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 6, "Top should update after pop")
        self.assertEqual(self.stack.get_max(), 6, "Max should update after pop")

    def test_pop_removes_max(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.pop()  # Removes 20
        self.assertEqual(self.stack.get_max(), 10, "Max should update when the maximum value is popped")

    def test_get_max_empty_stack(self):
        self.assertIsNone(self.stack.get_max(), "get_max should return None for an empty stack")

    def test_top_empty_stack(self):
        self.assertIsNone(self.stack.top(), "Top should return None for an empty stack")

    def test_pop_empty_stack(self):
        self.assertIsNone(self.stack.pop(), "Pop should handle an empty stack gracefully")

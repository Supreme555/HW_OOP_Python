import unittest
from my_queue import Queue

# [1, 5, 2]
class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()
        self.queue.append(1)
        self.queue.append(5)
        self.queue.append(2)

    def test_pop_non_empty(self) -> None:
        x = self.queue.pop_front()
        self.assertEqual(x, 1)

    def test_pop_empty(self) -> None:
        q = Queue()
        x = q.pop_front()
        self.assertIs(x, None)

    def test_size_non_empty(self):
        s = self.queue.size()
        self.assertEqual(s, 3)

    def test_size_empty(self):
        q = Queue()
        s = q.size()
        self.assertEqual(s, 0)
        
    def test_is_empty_true(self):
        q = Queue()
        self.assertTrue(q.is_empty())
    
    def test_is_empty_false(self):
        self.assertFalse(self.queue.is_empty())

    def test_peak_not_empty(self):
        self.assertEqual(self.queue.peak(), 1)

    def test_peak_empty(self):
        q = Queue()
        self.assertIs(q.peak(), None)

if __name__ == "__main__":
    unittest.main()
"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "[1, 2]")

    def test_str_empty_queue(self):
        self.assertEqual(str(self.queue), "[]")

    def test_str_non_empty_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "[1, 2]")

if __name__ == "__main__":
    unittest.main()
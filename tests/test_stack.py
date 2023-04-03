"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning({'a': 1})
        self.assertEqual(str(self.ll), " {'a': 1} -> None")
        self.ll.insert_beginning({'b': 2})
        self.assertEqual(str(self.ll), " {'b': 2} -> {'a': 1} -> None")

    def test_insert_at_end(self):
        self.ll.insert_at_end({'a': 1})
        self.assertEqual(str(self.ll), " {'a': 1} -> None")
        self.ll.insert_at_end({'b': 2})
        self.assertEqual(str(self.ll), " {'a': 1} -> {'b': 2} -> None")

    def test_str(self):
        self.assertEqual(str(self.ll), "None")
        self.ll.insert_beginning({'a': 1})
        self.assertEqual(str(self.ll), " {'a': 1} -> None")
        self.ll.insert_beginning({'b': 2})
        self.assertEqual(str(self.ll), " {'b': 2} -> {'a': 1} -> None")


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top.data, 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top.data, 2)

    def test_pop(self):
        with self.assertRaises(Exception):
            self.stack.pop()
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.top.data, 1)


if __name__ == '__main__':
    unittest.main()
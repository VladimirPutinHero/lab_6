import unittest
from lab_6 import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(str(llist), "1 2 3 ")

    def test_sort_list(self):
        llist = LinkedList()
        llist.append(3)
        llist.append(1)
        llist.append(2)
        llist.sort_list()
        self.assertEqual(str(llist), "1 2 3 ")


if __name__ == '__main__':
    unittest.main()

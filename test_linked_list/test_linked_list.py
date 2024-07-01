import unittest
from LinkedListClass import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_at_head(self):
        self.linked_list.insert_at_head(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.linked_list.insert_at_head(2)
        self.assertEqual(self.linked_list.head.data, 2)

    def test_insert_at_end(self):
        self.linked_list.insert_at_end(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.linked_list.insert_at_end(2)
        self.assertEqual(self.linked_list.head.next_node.data, 2)

    def test_remove_node_position(self):
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(2)
        self.assertEqual(self.linked_list.remove_node_position(2), "Удален узел с данными 2 позиции 2")
        self.assertEqual(self.linked_list.head.data, 1)

    def test_insert_at_position(self):
        self.linked_list.insert_at_end(1)
        self.assertEqual(self.linked_list.insert_at_position(2, 2), "Узел с данными 2 добавлен на позицию 2")
        self.assertEqual(self.linked_list.head.next_node.data, 2)

    def test_print_ll(self):
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(2)
        self.assertEqual(self.linked_list.print_ll(), "Данные списка выведены")

    def test_get(self):
        self.linked_list.insert_at_end(1)
        self.assertTrue(self.linked_list.get(1)[0])
        self.assertFalse(self.linked_list.get(2)[0])

    def test_change_data(self):
        self.linked_list.insert_at_end(1)
        self.assertEqual(self.linked_list.change_data(1, 2), "Заменены данные в узле № 1")
        self.assertEqual(self.linked_list.head.data, 2)

    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.linked_list.insert_at_end(1)
        self.assertFalse(self.linked_list.is_empty())

    def test_is_full(self):
        self.assertFalse(self.linked_list.is_full())
        for _ in range(self.linked_list.max_size):
            self.linked_list.insert_at_end(1)
        self.assertTrue(self.linked_list.is_full())

    def test_dequeue(self):
        self.linked_list.insert_at_end(1)
        self.assertEqual(self.linked_list.dequeue(), 1)
        self.assertEqual(self.linked_list.dequeue(), "Очередь пуста")

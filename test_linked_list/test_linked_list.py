import unittest
from unittest.mock import patch
from LinkedListClass import LinkedList
import io


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Инициализация нового связного списка для тестирования."""
        self.linked_list = LinkedList()

    def test_insert_at_head(self):
        """Тестирование добавления узлов в начало списка."""
        self.assertEqual(self.linked_list.insert_at_head(1), "Узел с данными 1 добавлен в начало списка")
        self.assertEqual(self.linked_list.insert_at_head(2), "Узел с данными 2 добавлен в начало списка")
        self.assertEqual(self.linked_list.insert_at_head(3), "Узел с данными 3 добавлен в начало списка")
        self.assertEqual(self.linked_list.head.data, 3)  # Проверка, что голова списка содержит 3

    def test_insert_at_end(self):
        """Тестирование добавления узлов в конец списка."""
        self.linked_list.insert_at_head(1)
        self.linked_list.insert_at_head(2)
        self.assertEqual(self.linked_list.insert_at_end(3), "Узел с данными 3 добавлен в конец списка")
        self.assertEqual(self.linked_list.head.next_node.data,
                         1)  # Проверка, что следующий узел после головы содержит 1

    def test_remove_node_position(self):
        """Тестирование удаления узла по позиции."""
        self.linked_list.insert_at_head(1)  # 1
        self.linked_list.insert_at_head(2)  # 2
        self.linked_list.insert_at_head(3)  # 3
        # Теперь порядок: 3 -> 2 -> 1
        self.assertEqual(self.linked_list.remove_node_position(2), "Удален узел с данными 2 позиции 2")
        self.assertEqual(self.linked_list.head.next_node.data,
                         1)  # Проверка, что следующий узел после головы содержит 1

    def test_insert_at_position(self):
        """Тестирование добавления узла на заданную позицию."""
        self.linked_list.insert_at_head(1)
        self.linked_list.insert_at_head(2)
        self.assertEqual(self.linked_list.insert_at_position(3, 2), "Узел с данными 3 добавлен на позицию 2")
        self.assertEqual(self.linked_list.head.next_node.data, 3)  # Проверка, что второй узел содержит 3

    def test_change_data(self):
        """Тестирование изменения данных в узле."""
        self.linked_list.insert_at_head(1)
        self.linked_list.insert_at_head(2)
        self.assertEqual(self.linked_list.change_data(1, 3), "Заменены данные в узле № 2")
        self.assertEqual(self.linked_list.head.next_node.data, 3)  # Проверка, что данные изменены на 3

    def test_get(self):
        """Тестирование поиска узла с данными."""
        self.linked_list.insert_at_head(1)
        self.linked_list.insert_at_head(2)
        found, node = self.linked_list.get(1)
        self.assertTrue(found)  # Данные должны быть найдены
        self.assertEqual(node.data, 1)  # Проверка, что найденный узел содержит 1

    def test_print_ll(self):
        """Тестирование вывода данных списка."""
        self.linked_list.insert_at_head(1)
        self.linked_list.insert_at_head(2)
        self.linked_list.insert_at_head(3)

        # Перехват вывода
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.linked_list.print_ll()
            output = fake_out.getvalue().strip()  # Получаем вывод

        # Проверяем, что вывод содержит ожидаемые данные
        self.assertEqual(output, "3\n2\n1")  # Проверка на правильный вывод


if __name__ == '__main__':
    unittest.main()
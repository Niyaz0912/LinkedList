import unittest
from QueueClass import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        """Инициализация очереди размером 5 для тестирования."""
        self.queue = Queue(5)

    def test_is_empty(self):
        """Тестирование метода проверки на пустоту очереди."""
        self.assertTrue(self.queue.is_empty())  # Изначально очередь должна быть пустой

    def test_is_full(self):
        """Тестирование метода проверки на заполненность очереди."""
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.queue.enqueue('d')
        self.queue.enqueue('e')
        self.assertTrue(self.queue.is_full())  # После добавления 5 элементов очередь должна быть полной

    def test_enqueue(self):
        """Тестирование добавления элементов в очередь."""
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.assertEqual(self.queue.queue, ['a', 'b'])  # Проверка содержимого очереди

    def test_dequeue(self):
        """Тестирование удаления элементов из очереди."""
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        removed = self.queue.dequeue()
        self.assertEqual(removed, 'a')  # Должен вернуть 'a'
        self.assertEqual(self.queue.queue, ['b'])  # Проверка содержимого очереди

    def test_dequeue_empty(self):
        """Тестирование удаления элемента из пустой очереди."""
        removed = self.queue.dequeue()
        self.assertIsNone(removed)  # Должен вернуть None
        self.assertTrue(self.queue.is_empty())  # Очередь должна оставаться пустой

    def test_enqueue_full(self):
        """Тестирование добавления элемента в полную очередь."""
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.queue.enqueue('d')
        self.queue.enqueue('e')
        self.queue.enqueue('f')  # Попытка добавить в полную очередь
        self.assertEqual(len(self.queue.queue), 5)  # Размер очереди должен оставаться 5


if __name__ == '__main__':
    unittest.main()

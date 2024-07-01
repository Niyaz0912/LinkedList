class CharQueue:
    """
    Реализация очереди для работы с символьными значениями.

    Атрибуты:
    max_size (int): Максимальный размер очереди.
    queue (list): Список, хранящий элементы очереди.
    front (int): Индекс первого элемента в очереди.
    rear (int): Индекс последнего элемента в очереди.
    count (int): Количество элементов в очереди.
    """

    def __init__(self, max_size):
        """
        Инициализирует очередь с заданным максимальным размером.

        Args:
        max_size (int): Максимальный размер очереди.
        """
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        """
        Проверяет, является ли очередь пустой.

        Returns:
        bool: True, если очередь пуста, False в противном случае.
        """
        return self.count == 0

    def is_full(self):
        """
        Проверяет, является ли очередь заполненной.

        Returns:
        bool: True, если очередь заполнена, False в противном случае.
        """
        return self.count == self.max_size

    def enqueue(self, item):
        """
        Добавляет элемент в конец очереди.

        Args:
        item (str): Элемент, который нужно добавить в очередь.

        Raises:
        ValueError: Если очередь заполнена.
        """
        if self.is_full():
            raise ValueError("Очередь заполнена")
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        """
        Удаляет и возвращает элемент из начала очереди.

        Returns:
        str: Элемент, который был удален из очереди.

        Raises:
        ValueError: Если очередь пуста.
        """
        if self.is_empty():
            raise ValueError("Очередь пуста")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.count -= 1
        return item

    def show(self):
        """
        Отображает все элементы очереди.
        """
        if self.is_empty():
            print("Очередь пуста")
        else:
            print("Элементы очереди:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i % self.max_size])
class Node:
    """Класс Node - это узел в связном списке"""

    def __init__(self, data, next_node=None):
        """Функция инициализирует узел. Здесь data: данные узла next_node: ссылка на следующий узел"""
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс LinkedList - это реализация связного списка"""

    def __init__(self, max_size=5):
        """Инициализирует пустой список"""
        self.head = None
        self.end = None
        self.max_size = max_size

    def insert_at_head(self, data):
        """Функция добавляет узел с данными в начало списка. В data добавляются данные.
        Возвращает сообщение об успешном добавлении узла"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):
        """Функция добавляет узел в конец списка. В data добавляются данные.
        Возвращает сообщение об успешном добавлении узла"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):
        """Функция удаляет узел по позиции. В rm указывается позиция узла.
        Возвращает сообщение об успешном удалении узла. Если узел не обнаружен, сообщает 'Ничего не удалено"""
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):
        """Функция добавляет узел с данными на заданную позицию. Возвращает сообщение об успешном добавлении узла"""
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            new_node.next_node = self.head
            self.head = new_node
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        """Опционально"""
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        """Если есть опционально (код выше то следующие 2 строки не нужны)"""
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):
        """Функция выводит данные списка"""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):
        """Функция ищет узел с данными. Возвращает True если найдены False - если нет"""
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):
        """Функция изменяет данные в узле. Здесь node_data: данные для изменения change_data: новые данные.
        Возвращает сообщение об успешном изменении данных или данные не обнаружены - если позиция не найдена"""
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"


# Создаем экземпляр класса LinkedList
linked_list = LinkedList()

# Добавляем узлы в начало списка
print(linked_list.insert_at_head(1))  # Узел с данными 1 добавлен в начало списка
print(linked_list.insert_at_head(2))  # Узел с данными 2 добавлен в начало списка
print(linked_list.insert_at_head(3))  # Узел с данными 3 добавлен в начало списка

# Добавляем узлы в конец списка
print(linked_list.insert_at_end(4))  # Узел с данными 4 добавлен в конец списка
print(linked_list.insert_at_end(5))  # Узел с данными 5 добавлен в конец списка

# Выводим данные списка
print(linked_list.print_ll())

# Удаляем узел по позиции
print(linked_list.remove_node_position(3))  # Удален узел с данными 1 позиции 3

# Добавляем узел на заданную позицию
print(linked_list.insert_at_position(6, 3))  # Узел с данными 6 добавлен на позицию 3

# Изменяем данные в узле
print(linked_list.change_data(5, 7))  # Заменены данные в узле № 5

# Выводим данные списка
print(linked_list.print_ll())

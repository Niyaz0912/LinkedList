class Queue:

    def __init__(self, size):

        self.size = size
        self.queue = []

    def is_empty(self):

        return len(self.queue) == 0

    def is_full(self):

        return len(self.queue) == self.size

    def enqueue(self, char):

        if not self.is_full():
            self.queue.append(char)
        else:
            print("Очередь заполнена!")

    def dequeue(self):

        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Очередь пуста!")
            return None

    def show(self):

        print("Содержимое очереди:", self.queue)


def display_menu():

    print("Меню:")
    print("1. Добавить элемент в очередь")
    print("2. Удалить элемент из очереди")
    print("3. Проверить, пуста ли очередь")
    print("4. Проверить, заполнена ли очередь")
    print("5. Показать содержимое очереди")
    print("6. Выход")


if __name__ == '__main__':
    q = Queue(5)
    while True:
        display_menu()
        choice = input("Введите ваш выбор (1-6): ")

        if choice == '1':
            char = input("Введите символ для добавления в очередь: ")
            q.enqueue(char)
        elif choice == '2':
            removed = q.dequeue()
            if removed:
                print(f'Удален: {removed}')
        elif choice == '3':
            print("Очередь пуста?", q.is_empty())
        elif choice == '4':
            print("Очередь заполнена?", q.is_full())
        elif choice == '5':
            q.show()
        elif choice == '6':
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите снова!")

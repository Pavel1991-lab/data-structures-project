class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий узел
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        """Добавление элемента в конец очереди"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail is None:
            self.tail = new_node
            self.head.next_node = self.tail
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        result = []
        node = self.head
        while node is not None:
            result.append(str(node.data))
            node = node.next_node
        return "[" + ", ".join(result) + "]"

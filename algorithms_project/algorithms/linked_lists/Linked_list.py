class Node:
    def __init__(self, value):
        self.value = value      # valor guardado no nó
        self.next = None        # referência para o próximo nó
        self.prev = None        # referência para o nó anterior


class DoublyLinkedList:
    def __init__(self):
        self.head = None        # inicio da lista ou a "cabeça"
        self.tail = None       # fim da lista ou "rabo"

    def add_to_front(self, value):  # ********* 👉 Coloca alguém na frente da fila. ******************
        new_node = Node(value)                  # Cria um novo nó
        if not self.head:                       # Se a lista estiver vazia
            self.head = self.tail = new_node
        else:
            new_node.next = self.head           # Novo nó aponta para o antigo começo
            self.head.prev = new_node           # antigo começo aponta para o novo nó
            self.head = new_node               # atualiza o começo

    def add_to_end(self, value):  # ********* 👉 Coloca alguém no fim da fila. ******************
        new_node = Node(value)
        if not self.tail:                       # se a lista estiver vazia
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail          # novo nó aponta para o antigo fim
            self.tail.next = new_node           # antigo fim aponta para o novo nó
            self.tail = new_node                # atualiza o fim

    def remove_from_front(self):  # ********* 👉 Remove o primeiro da fila. ******************
        if not self.head:
            return None                         # confere se a lista não está vazia
        removed_value = self.head.value         # guarda o valor removido
        if self.head == self.tail:              # só tinha 1 nó
            self.head = self.tail = None
        else:
            self.head = self.head.next          # move o head pro próximo
            self.head.prev = None               # o novo começo não tem anterior
        return removed_value

    def remove_from_end(self):  # ********* 👉 Remove o ultimo da fila. ******************
        if not self.tail:
            return None                         # confere se a lista não está vazia
        removed_value = self.tail.value         # guarda o valor removido
        if self.head == self.tail:              # só tinha 1 nó
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev          # move o tail pro anterior
            self.tail.next = None               # o novo fim não tem próximo
        return removed_value

    def to_list(self):  # ********* Só percorre e devolve os valores como lista Python [1,2,3,...]. ******************
        current = self.head
        items = []
        while current:
            items.append(current.value)         # percorre do começo até o fim
            current = current.next
        return items
    
    def current_tail(self):
                   # Cria um novo nó
        if not self.head:                       # Se a lista estiver vazia
            return None
        else:
            return self.head


dll = DoublyLinkedList()


dll = DoublyLinkedList()

dll.add_to_front(3)   # Lista: [3]
dll.add_to_front(2)   # Lista: [2, 3]
dll.add_to_front(1)   # Lista: [1, 2, 3]

dll.add_to_end(4)     # Lista: [1, 2, 3, 4]
dll.add_to_end(5)     # Lista: [1, 2, 3, 4, 5]

print(dll.to_list())  # 👉 [1, 2, 3, 4, 5]

print(dll.remove_from_front())  # 👉 remove 1
print(dll.remove_from_end())    # 👉 remove 5

print(dll.to_list())  # 👉 [2, 3, 4]

import queue
from queue import Queue
from collections import deque

q = Queue()

q.put(1)
q.put(2)
q.put(3)

print(f"uma queue {q}")

print(q.get())
print(q.get())

fila = queue.Queue(maxsize=5)

fila.put("A")
fila.put("B")
fila.put("C")

print("Fila cheia?", fila.full())

print("Removido:", fila.get())
print("Removido:", fila.get())

print("Fila vazia?", fila.empty())

print("Tamanho da fila:", fila.qsize())


pedidos = queue.Queue()

pedidos.put("Pedido1")
pedidos.put("Pedido2")
pedidos.put("Pedido3")

while not pedidos.empty():
    atual = pedidos.get()
    print(f"Atendendo {atual}")


"""
Exemplos com Dequeue:

"""

fila = deque()

fila.append("Joao")
fila.append("Maria")
fila.append("Pedro")

print(fila.popleft())
print(fila.popleft())

print(fila)

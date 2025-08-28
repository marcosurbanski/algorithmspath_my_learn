"""
Este código implementa duas versões de busca exponencial em arrays ordenados,
uma usando acesso direto ao array e outra simulando o ArrayReader do LeetCode 702.

Objetivo:
- A classe Solution implementa a busca exponencial diretamente em um array normal.
- A classe Solution1 implementa a busca exponencial em um array de tamanho desconhecido
  usando a interface ArrayReader, combinando exponential search com binary search.
- A classe ArrayReader simula a interface usada no LeetCode, retornando um valor
  muito grande caso o índice acessado esteja fora do limite.
"""


# Simula o ArrayReader do LeetCode
class ArrayReader:
    def __init__(self, arr):
        # Armazena o array interno
        self.arr = arr

    def get(self, index: int) -> int:
        # Se o índice está dentro do array, retorna o valor correspondente
        if 0 <= index < len(self.arr):
            return self.arr[index]
        # Caso contrário, retorna um valor muito grande (simulando índice fora do array)
        return 2**31 - 1


# Implementação de Exponential Search com acesso direto ao array
class Solution():
    @staticmethod
    def binary_search(nums, n, low, high):
        """
        Busca binária em um array ordenado entre os índices low e high.
        Retorna o índice do elemento n ou -1 se não encontrado.
        """
        while low < high:
            # Calcula o índice do meio do intervalo
            mid = int((low + high)/2)

            if nums[mid] == n:
                # Encontrou o elemento
                return mid
            elif nums[mid] < n:
                # Elemento está à direita
                low = mid + 1
            else:
                # Elemento está à esquerda
                high = mid
        # Não encontrou o elemento
        return -1

    def exponencial_search(self, arr, target):
        """
        Busca exponencial em um array ordenado.
        Primeiro encontra um intervalo em que o target pode estar,
        depois aplica busca binária nesse intervalo.
        """
        # Caso o primeiro elemento seja o target
        if arr[0] == target:
            return 0
        n = len(arr)
        i = 1

        # Dobrar o índice até ultrapassar o target ou o tamanho do array
        while i < n and arr[i] < target:
            i *= 2

        # Caso o elemento esteja exatamente no índice encontrado
        if arr[i] == target:
            return i

        # Aplicar busca binária no intervalo encontrado
        return Solution.binary_search(arr, target, i//2, min(i, n-1))


# Implementação de Exponential Search usando ArrayReader (tamanho desconhecido)
class Solution1():
    def search(self, reader: ArrayReader, target: int) -> int:
        # Caso base: verifica o primeiro elemento
        if reader.get(0) == target:
            return 0

        # 1) Busca exponencial para encontrar o intervalo
        i = 1
        while reader.get(i) < target:
            # Dobrar o índice até encontrar valor >= target
            i *= 2

        # 2) Busca binária dentro do intervalo [i//2, i]
        low, high = i // 2, i
        while low <= high:
            # Índice do meio do intervalo
            mid = (low + high) // 2
            # Valor no índice mid
            val = reader.get(mid)

            if val == target:
                # Encontrou o target
                return mid
            elif val > target:
                # Target está à esquerda
                high = mid - 1
            else:
                # Target está à direita
                low = mid + 1

        # Target não encontrado
        return -1

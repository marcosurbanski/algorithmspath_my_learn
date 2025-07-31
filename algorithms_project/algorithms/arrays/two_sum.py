from typing import List

class Problem1:
    def two_sum(self, A: List[int], k: int) -> List[int]:
        n = len(A)
        result = [-1, -1]
        min_j = n  # para controlar o menor j encontrado
        
        # Percorrer todos os pares i<j
        for j in range(1, n):
            for i in range(j-1, -1, -1):  # i máximo para mínimo j, percorre i de trás para frente
                if A[i] + A[j] == k:
                    if j < min_j or (j == min_j and i > result[0]):
                        result = [i, j]
                        min_j = j
                    break  # para i, não precisa buscar mais i menores, pois queremos i máximo para esse j
        return result
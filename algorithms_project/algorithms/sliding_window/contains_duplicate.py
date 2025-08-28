"""
Sliding Window 
219. Contains Duplicate II

Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

"""


class Numsolution(object):
    def containnumsNearbyDuplicate(self, nums, k):
        """
        Verifica se existe algum par de elementos duplicados na lista 'nums'
        tal que os índices desses elementos estejam a no máximo 'k' posições de distância.
        
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # Começamos com o primeiro índice da lista
        i = 0

        # Loop externo percorre cada elemento da lista como possível "primeiro duplicado"
        while i < len(nums):
            # 'j' começa logo após 'i' e vai até 'i + k' ou até o final da lista
            j = i + 1
            while j <= i + k and j < len(nums):
                # Imprime quais elementos estão sendo comparados (útil para depuração)
                print(f'Comparando nums[{i}] = {nums[i]} com nums[{j}] = {nums[j]}')
                
                # Se encontrar duplicata dentro da janela de tamanho k, retorna True
                if nums[i] == nums[j]:
                    return True
                
                # Avança o segundo índice
                j += 1
            
            # Avança o primeiro índice
            i += 1
        
        # Se percorreu toda a lista e não encontrou duplicatas próximas, retorna False
        return False

class Solution():
    def containsnumsNearbyDuplicate2(self, nums, k):
        """
        Verifica se existe algum par de elementos duplicados na lista 'nums'
        tal que os índices desses elementos estejam a no máximo 'k' posições de distância.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Verifica se a diferença de índices é menor ou igual a k
                if abs(i - j) <= k:
                    print(f'Comparando nums[{i}] = {nums[i]} com nums[{j}] = {nums[j]}')
                    if nums[i] == nums[j]:
                        return True
                else:
                    # Como j só aumenta, se a diferença já passou de k, não precisa continuar
                    break
        return False                        
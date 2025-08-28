"""
1. Two Sum

HashMap:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Encontra dois indices em 'nums' cuja soma seja 'target'.


lógica principal (intituitiva):

- Para cada número atual, calculamos o 'complemento' que falta
  para atingir o target: complemento = target - num.

- Perguntamos: "Já vimos esse complemento antes?".
    -> Se sim: encontramos o par e retornamos os indices.
    -> Se não: guardamos o número atual no dicionario e seguimos.

- O dicionário funciona como uma mémoria de números já vistos.

- A soma real acontece de forma implicita quando encontramos o complemento no dicionário.

-O complemento atual é o valor que falta para atingir o target.
    Para cada número num em nums, calculamos:
        complemento = target - num

verifica no dicionario se este valor ja foi visto antes.
    num + complemento = target
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # dicionário para armazenar {valor: índice}

        for i, num in enumerate(nums):  # percorre cada número da lista com seu índice
            complemento = target - num  # calcula o número que falta para atingir o target

            if complemento in num_dict:
                # Se o complemento já foi visto antes, encontramos a resposta
                return [num_dict[complemento], i]

            # Caso contrário, guardamos o número atual no dicionário
            num_dict[num] = i

        # Só por segurança (no LeetCode sempre existe solução)
        return [-1, -1]


solutions = Solution()
a = [2, 7, 11, 15]
target = 17

print(solutions.twoSum(a, target))

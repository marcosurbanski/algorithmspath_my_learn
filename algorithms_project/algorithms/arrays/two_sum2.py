"""
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
        num_dict = {}

        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in num_dict:
                return [num_dict[complemento], i]
            num_dict[num] = i

        return [-1, -1]

solutions = Solution()
a = [2,7,11,15]
target = 17

print(solutions.twoSum(a, target))





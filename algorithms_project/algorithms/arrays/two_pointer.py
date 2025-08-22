class Solution:
    def reverseWords_manual(string_word):
        res = ''  # Para realizar o reverse da string cria-se uma substring
        left, right = 0, 0  # Inici-ase os ponteiros left e right em zero

        while right < len(string_word):  # loop dentro do tamanho da string
            if string_word[right] != ' ':  # enquanto a posição de right dentro da string for diferente de espaço em branco
                right += 1  # incrementa o right para continuar o loop
            else:  # caso encontre um espaço vazio
                res += string_word[left:right+1][::-1]  # sera adicionado os valores na substring dos ponteiros left e right invertidos [::-1]
                right += 1  # incrementa +1 no right para sair do espaço vazio e iniciar a leitura da proxima palavra
                left = right

        res += ' '  # pula um espaço na substring para acrescentar a proxima palavra
        res += string_word[left:right + 2][::-1]  # adicina a proxima palavra na substring acrescenta o 2porque saiu fora do loop acima e reverte
        return res[1:]  # começa da posição 1 devido ter um espaço em branco no começo


cat = Solution.reverseWords_manual("rac tar")
print(cat)


class Solution2:
    def reverserWords(s):
        return ' '.join(word[::-1] for word in s.split())  # utilizando modulo pronto da linguagem para resolver


reverseword = Solution2.reverserWords("I evol edocteel")
print(reverseword)


class Solution3:
    def reverseWords_manual1(sword: str) -> str:
        res = ''
        left = 0
        for right in range(len(sword) + 1):
            # Percorre todos os índices da string + 1 (para capturar o último "fim de palavra")
            if right == len(sword) or sword[right] == ' ':
                # Se chegamos no final da string OU encontramos um espaço (fim de palavra):
                res += sword[left:right][::-1]
                # Pega a palavra entre left e right, inverte ( [::-1] ) e adiciona ao resultado
                if right < len(sword):
                    res += ' '
                    # Se não for o último caractere, adiciona um espaço ao resultado
                left = right + 1
                # Move o ponteiro 'left' para o início da próxima palavra
        return res


reverseword3 = Solution3.reverseWords_manual1("Let's take LeetCode contest")
print(reverseword3)

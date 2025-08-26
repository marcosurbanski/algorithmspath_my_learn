"""
Este código implementa duas soluções diferentes para o problema
"Length of Last Word" (LeetCode 58).

Objetivo:
Dada uma string que contém palavras e espaços, retornar o comprimento
da última palavra (sequência de caracteres não vazios separados por espaços).

A classe Solution resolve o problema manualmente usando ponteiros (left e right).
A classe Solution2 resolve de forma mais simples usando o método split() do Python.
"""


class Solution():
    def lengthOfLastWord(self, string_word: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # Incializa os poneiros left e right em 0
        left, right = 0, 0
        # Lista para armazenar as palavras encontradas
        words = []

        # Loop percorre a string até o final
        while right < len(string_word):
            # Se o caractere atual não for espaço, move o ponteiro da direita
            if string_word[right] != ' ':
                right += 1
            else:
                # Caso encontre espaço, adiciona a palavra entre left e right
                words.append(string_word[left:right])
                # Avança o ponteiro right para pular o espaço
                right += 1
                # Atualiza o ponteiro left para o próximo inicio de palavra
                left = right
        # após o loop, adiciona a ultima palavra capturada
        words.append(string_word[left:right])
        # Retorna o tamanho da última palavra capturada
        return len(words[-1])


class Solution2():
    def lengthOfLastWord(self, string_word: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # Usa split() para separar a string em palavras igorando múltiplos espaços
        words = string_word.split()
        # Retorna o comprimento da última palavra
        return len(words[-1])

class Solution:
    def maximumLengthSubstring(self, string_word: str) -> int:
        """
        Find the maximum length substring where no character appears more than twice
        / Encontra o comprimento máximo de uma substring onde nenhum caractere aparece mais de duas vezes.

        Args:
            string_word (str): The input string to analyze
            / A string de entrada para analisar.

        Returns:
            int: The length of the longest valid substring
            / O comprimento da substring válida mais longa.
        """

        left, right = 0, 0  # Initialize window pointers / Inicializa os ponteiros da janela
        _max = 1  # Maximum length found / Maior comprimento encontrado
        counter = {}  # Dictionary to count characters / Dicionário para contar caracteres

        counter[string_word[0]] = 1  # Count first character / Conta o primeiro caractere
        while right < len(string_word) - 1:  # While right pointer is within string / Enquanto o ponteiro direito estiver dentro da string
            right += 1  # Move right pointer / Move o ponteiro direito

            if counter.get(string_word[right]):  # If character already in counter / Se o caractere já está no contador
                counter[string_word[right]] += 1  # Increment its count / Incrementa a contagem
            else:
                counter[string_word[right]] = 1  # Otherwise initialize count / Caso contrário, inicializa a contagem

            while counter[string_word[right]] == 3:  # While character appears 3 times / Enquanto o caractere aparecer 3 vezes
                counter[string_word[left]] -= 1  # Decrease count of leftmost char / Diminui a contagem do caractere mais à esquerda
                left += 1  # Move left pointer / Move o ponteiro esquerdo

            _max = max(_max, right - left + 1)  # Update maximum length / Atualiza o comprimento máximo

        return _max  # Return maximum length / Retorna o comprimento máximo

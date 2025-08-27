class Solution:
    # Define uma classe chamada Solution (estrutura comum usada no LeetCode)
    def firstUniqChar(self, s: str) -> int:
        # Método que recebe uma string 's' e retorna o índice do primeiro caractere único
        # (que aparece apenas uma vez). Se não houver, retorna -1.

        d = {}
        # Cria um dicionário vazio 'd' que vai armazenar cada caractere da string
        # como chave, e como valor uma lista [índice, contagem].

        for idx, ch in enumerate(s):
            # Percorre cada caractere 'ch' da string 's', junto com seu índice 'idx'.

            if not d.get(ch):
                # Se o caractere ainda não existe no dicionário...

                d[ch] = [idx, 1]
                # Adiciona o caractere no dicionário com:
                # [índice da primeira ocorrência, contagem inicial 1].

            else:
                d[ch][1] += 1
                # Caso o caractere já esteja no dicionário, incrementa a contagem em +1.

        for ch, val in d.items():
            # Percorre os pares (caractere, [índice, contagem]) armazenados no dicionário.

            if val[1] == 1:
                # Se a contagem (val[1]) for igual a 1, significa que o caractere é único.

                return val[0]
                # Retorna o índice (val[0]) da primeira ocorrência desse caractere único.

        return -1
        # Se não encontrar nenhum caractere único, retorna -1.

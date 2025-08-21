class Binary:
    @staticmethod
    def binary_search(nums, target):
        """
        Perform a binary search on a sorted list / Realiza uma busca binária em uma lista ordenada.
        Args:
            nums (list): A sorted list of numbers / Uma lista ordenada de números
            target (int): The value to search for / O valor a ser procurado
        Returns:
            int: Steps to find target, or -1 if not found / Passos para encontrar o alvo, ou -1 se não encontrado
        """

        low = 0  # Starting index / Índice inicial
        high = len(nums) - 1  # Ending index / Índice final
        steps = 0  # Step counter / Contador de passos

        while low <= high:  # While range is valid / Enquanto o intervalo for válido
            steps += 1  # Count step / Conta o passo
            mid = (low + high) // 2  # Middle index / Índice do meio
            if nums[mid] == target:  # Target found / Alvo encontrado
                return steps  # Return steps / Retorna passos
            elif nums[mid] < target:  # Middle smaller than target / Meio menor que alvo
                low = mid + 1  # Search right / Busca à direita
            else:  # Middle larger than target / Meio maior que alvo
                high = mid - 1  # Search left / Busca à esquerda
        return -1  # Target not found / Alvo não encontrado

class Binary:
    # Define uma classe chamada Binary (apenas para organizar o método).
    # Define a class called Binary (just to organize the method)

    def binary_search(nums,  target):
        """
        Define o método binary_search que recebe:
            - nums: lista de números ordenados
            - n: valor alvo (target) que queremos encontrar
        Define the method binary_search which receives:
            - nums: a sorted list
            - target: The value to search for
        """
        low = 0
        high = len(nums) - 1
        steps = 0

        while low <= high:
            steps += 1
            mid = (low + high) // 2

            if nums[mid] == target:
                return steps
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

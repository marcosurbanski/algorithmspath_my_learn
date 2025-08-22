class Solution():
    def lengthOfLastWord(self, string_word: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0        
        words = []

        while right < len(string_word):
            if string_word[right] != ' ':
                right += 1                
            else:
                words.append(string_word[left:right])
                right += 1
                left = right
                
        words.append(string_word[left:right])
        
        return len(words[-1])
            

class Solution:
    def reverseWords_manual(string_word):
        res = ''
        left, right = 0, 0

        while right < len(string_word):
            if string_word[right] != ' ':
                right += 1
            else:
                res += string_word[left:right+1][::-1]
                right += 1
                left = right

        res += ' '
        res += string_word[left:right + 2][::-1]
        return res[1:]


cat = Solution.reverseWords_manual("rac tar")
print(cat)


class Solution2:
    def reverserWords(s):
        return ' '.join(word[::-1] for word in s.split())


reverseword = Solution2.reverserWords("I evol edocteel")
print(reverseword)


class Solution3:
    def reverseWords_manual1(s):
        res = ''
        for right in range(len(s) + 1):
            if right == len(s) or s[right] == ' ':
                res += s[:right][::-1]
                if right < len(s):
                    res += ' '
        return res


reverseword3 = Solution3.reverseWords_manual1("Let's take LeetCode contest")
print(reverseword3)

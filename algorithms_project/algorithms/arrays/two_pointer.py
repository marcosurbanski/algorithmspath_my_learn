class Solution:
    def reverseWords_manual(s):
        res = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                res += s[l:r+1][::-1]
                r += 1
                l = r
            
        res += ' '
        res += s[l:r + 2][::-1]
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
        l = 0
        for r in range(len(s) + 1):
            if r == len(s) or s[r] == ' ':
                res += s[l:r][::-1]
                if r < len(s):
                    res += ' '
                l = r + 1
        return res

reverseword3 = Solution3.reverseWords_manual1("Let's take LeetCode contest")
print(reverseword3)
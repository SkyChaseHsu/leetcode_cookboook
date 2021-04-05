# 字符串
class Solution:
    def reverseWords(self, s: str) -> str:
        s = [word[::-1] for word in s.split(" ")]
        return " ".join(s)
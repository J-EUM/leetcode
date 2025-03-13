class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [ch for ch in s]
        t_list = [ch for ch in t]

        s_list.sort()
        t_list.sort()

        return s_list == t_list
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1

        for ch in t:
            if s_dict.get(ch) is None:
                return False
            if s_dict.get(ch) > 1:
                s_dict[ch] -= 1
            else:
                s_dict.pop(ch)
        
        if s_dict:
            return False
        else:
            return True
        
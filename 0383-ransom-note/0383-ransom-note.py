class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sorted_ransom = sorted(ransomNote)
        sorted_magazine = sorted(magazine)

        while sorted_ransom and sorted_magazine:
            if sorted_ransom[-1] == sorted_magazine[-1]:
                sorted_ransom.pop()
                sorted_magazine.pop()
            else:
                sorted_magazine.pop()

        if sorted_ransom:
            return False
        return True

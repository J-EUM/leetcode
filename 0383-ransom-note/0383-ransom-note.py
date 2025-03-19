class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash = {}

        for c in magazine:
            magazine_hash[c] = magazine_hash.get(c, 0) + 1
        
        for c in ransomNote:
            magazine_hash[c] = magazine_hash.get(c, 0) - 1
            if magazine_hash[c] < 0:
                return False

        return True

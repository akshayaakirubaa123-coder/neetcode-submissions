class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        for word in s:
            s_map[word] = s_map.get(word, 0) + 1
        t_map = {}
        for word in t:
            t_map[word] = t_map.get(word, 0) + 1

        for char in t_map:
            if t_map[char] != s_map.get(char, 0):
                return False
        
        return True


        
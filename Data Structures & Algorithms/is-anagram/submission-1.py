from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_elements = s
        t_elements = t

        sort_s = sorted(s_elements)
        sort_t = sorted(t_elements)

        if sort_s == sort_t:
            return True
        return False

        
        
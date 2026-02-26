class Solution:
    def areIsomorphic(self, s1, s2):
        map1 = {}
        map2 = {}
        
        for c1, c2 in zip(s1, s2):
            
            if c1 in map1 and map1[c1] != c2:
                return False
            
            if c2 in map2 and map2[c2] != c1:
                return False
            
            map1[c1] = c2
            map2[c2] = c1
        
        return True
class Solution:
    def generateIp(self, s):
        res = []
        n = len(s)
        
        def backtrack(start, path):
            if len(path) == 4:
                if start == n:
                    res.append('.'.join(path))
                return
            
            # Try 1 to 3 digits
            for l in range(1, 4):
                if start + l > n:
                    break
                part = s[start:start+l]
                # Skip invalid parts
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                backtrack(start+l, path + [part])
        
        backtrack(0, [])
        return res if res else [-1]  # return [-1] if no valid IPs
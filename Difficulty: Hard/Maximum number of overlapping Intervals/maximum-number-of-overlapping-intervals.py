class Solution:
    def overlapInt(self, arr):
        events = []
        
        for start, end in arr:
            events.append((start, 1))
            events.append((end + 1, -1))
        
        events.sort()
        
        current = 0
        max_overlap = 0
        
        for time, change in events:
            current += change
            max_overlap = max(max_overlap, current)
        
        return max_overlap

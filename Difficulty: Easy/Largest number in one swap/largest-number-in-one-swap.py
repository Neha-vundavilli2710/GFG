class Solution:
    def largestSwap(self, s: str) -> str:
        arr = list(s)
        last = {int(ch): i for i, ch in enumerate(arr)}  # last occurrence of each digit
        
        n = len(arr)
        for i in range(n):
            for d in range(9, int(arr[i]), -1):  # check larger digits first
                if d in last and last[d] > i:
                    # Swap
                    arr[i], arr[last[d]] = arr[last[d]], arr[i]
                    return ''.join(arr)  # only one swap allowed
        return s  # no swap improves string
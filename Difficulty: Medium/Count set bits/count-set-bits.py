class Solution:
    def countSetBits(self, n: int) -> int:
        if n == 0:
            return 0

        x = n.bit_length() - 1
        p = 1 << x

        bits_up_to_2x = x * (p >> 1)
        msb_bits = n - p + 1
        rest = n - p

        return bits_up_to_2x + msb_bits + self.countSetBits(rest)

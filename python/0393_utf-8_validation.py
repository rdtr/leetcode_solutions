class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mask0 = 0b10000000
        mask1_1 = 0b11000000
        mask1_0 = 0b100000
        mask2_1 = 0b11100000
        mask2_0 = 0b10000
        mask3_1 = 0b11110000
        mask3_0 = 0b1000
        maskf = 0b10000000

        followingBytes = 0
        for byte in data:
            if followingBytes > 0:
                if byte & maskf != maskf:
                    return False
                followingBytes -= 1
                continue

            if byte & mask3_1 == mask3_1 and byte & mask3_0 == 0:
                followingBytes = 3
            elif byte & mask2_1 == mask2_1 and byte & mask2_0 == 0:
                followingBytes = 2
            elif byte & mask1_1 == mask1_1 and byte & mask1_0 == 0:
                followingBytes = 1
            elif byte & mask0 != 0:
                return False
        return followingBytes == 0
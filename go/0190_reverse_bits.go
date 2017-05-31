class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        i = 32
        while True:
            lastBit = n & 1
            res += lastBit
            
            i -= 1
            if i <= 0:
                break
            res, n = res << 1, n >> 1
        return res

cache = {}

class Solution:
    def reverseBit(self, n):
        res = 0
        i = 8
        while True:
            lastBit = n & 1
            res += lastBit
            
            i -= 1
            if i <= 0:
                break
            res, n = res << 1, n >> 1
        return res        
    
    
    def reverseBits(self, n):
        res = 0
        i = 0
        while True:
            shifted = n >> 8 * i
            b = shifted & 255 # extract 1 byte data
            
            if b in cache:
                rb = cache[b]
            else:
                rb = self.reverseBit(b)
                cache[b] = rb
            res += rb
            i += 1
            if i >= 4:
                break
            res = res << 8
        return res
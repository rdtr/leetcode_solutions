class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.convert(x) for x in range(1, n + 1)]

    def convert(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        return str(num)
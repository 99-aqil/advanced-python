class Solution:

    def findFactorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def printPattern(self):
        row = 5
        for i in range(1, row + 1):
            print("* " * i)
        j = row - 1
        while j > 0:
            print("* " * j)
            j -= 1
        return ""

    def itemCounter(self, arr):
        elements = {}
        for n in arr:
            if n in elements:
                elements[n] += 1
            else:
                elements[n] = 1
        return elements

    def removeSpecialSymbols(self, string):
        special_symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        s = ""
        for char in string:
            if char not in special_symbols:
                s += char
        return s


if __name__ == '__main__':
    solution = Solution()
    print("-----------------------------------------------------------------------------------")

    print("Output of problem 1:", solution.findFactorial(5))
    print("-----------------------------------------------------------------------------------")

    print("Output of problem 2:")
    print(solution.printPattern())
    print("-----------------------------------------------------------------------------------")

    _arr = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    print("Output of problem 3:", solution.itemCounter(_arr))
    print("-----------------------------------------------------------------------------------")

    print("Output of problem 4:", solution.removeSpecialSymbols("A(Q*I*(@L"))
    print("-----------------------------------------------------------------------------------")

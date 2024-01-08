class Solution:
    def __init__(self, file):
        
        lines = file.readlines()

        sum = 0

        for line in lines:
            l = line.strip()
            num = ''
            for n in l:
                if n.isdigit():
                    num += str(n)
            if len(num) == 1:
                num += str(num)
            elif len(num) > 2:
                first = num[0]
                second = num[len(num) - 1]
                num = str(first) + str(second)
            sum += int(num)

        print(sum)

file = open('test.txt', 'r')
ans = Solution(file)

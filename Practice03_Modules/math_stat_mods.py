import math
import random
import statistics

nums = [random.randint(0, 100) for i in range(10)]
print(*nums)

sumNums = math.fsum(nums)
mediumNums = statistics.mean(nums)
medianNums = statistics.median(nums)
devNums = statistics.stdev(nums)

print(sumNums)
print(mediumNums)
print(medianNums)
print("{:.2f}".format(devNums))
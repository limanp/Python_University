
# Task_14 -----------------------------------------

import math

print("Введіть число [N] (N > 1): ")
N = int(input())

if N > 1:
    K = 1
    minK = 1
    while K < N:
        if math.pow(5, K) > N:
            minK = K
            break
        K += 1
    print("Мінімальне число [K] при умові 5 ^ K > N =", minK)
else:
    print("Помилка!!! Введіть число [N] яке більше 1")

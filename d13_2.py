from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
#n = [7, 13, 19, 31, 59]
#b = [0, 1, 7, 6, 4]
n = [17, 37, 439, 29, 13, 23, 787, 41, 19]
b = [0, 11, 17, 19, 30, 40, 48, 58, 67]
a = [ n[i] - b[i] for i in range(len(n))]
print(chinese_remainder(n, a))

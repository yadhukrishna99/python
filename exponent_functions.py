def raise_pow(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result


x = int(input("Enter a base number: "))
y = int(input("Enter a power number: "))
print(raise_pow(x, y))

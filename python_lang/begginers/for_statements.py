# alphabet = ['a', 'b', 'c', 'd']

# for char in alphabet:
#     print(char)

# 0-9
# 0 1 2 3 4 ... 9
# for i in range(10, 2, -1):
#     print(i)


# {1, ..., 10}
for n in range(1, 100):
    if n == 1:
        continue
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} is not prime')
            break
    else:
        print(f'{n} is prime')
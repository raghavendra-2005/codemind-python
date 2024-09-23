def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num
N = int(input())
if is_fibonacci(N):
    print("True")
else:
    print("False")
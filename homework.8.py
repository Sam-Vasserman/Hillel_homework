def recursive(n):
    if n <= 1:
        return 1
    return n + recursive (n - 1)

print (recursive(5))
print (recursive(1))
print (recursive(0))    
print (recursive(10))
print (recursive(3))

def fibonacci(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print (fibonacci(10))
print (fibonacci(1))
print (fibonacci(0))
print (fibonacci(3))
print (fibonacci(7))

def multiply_list(list):
    if len(list) == 0:
        return 1
    else:
        return multiply_list(list[:-1]) * list[-1]


print(multiply_list([1, 2, 3, 4, 5]))
print(multiply_list([7, 2, 3, 6, 2]))
print(multiply_list([13, 9, 43, 65, 9]))
print(multiply_list([6, 2, 67, 34, 9]))
print(multiply_list([15, 1, 3, 16, 9]))

def natural (n):
    i = 1
    while i < n:
        i = i * 2
        if i == n:
            print("YES")
        else:
            print("NO")

natural(0)
natural(1)
natural(3)
natural(4)
natural(8)

def outer (a, b):
    def inner(a, b):
        return a + b
    return inner (a, b) + 5
    
print (outer(1, 4))
print (outer(0, 0))
print (outer(1, 1))
print (outer(12, 44))
print (outer(15, 23))
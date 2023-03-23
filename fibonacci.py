# 2 -----------------------

num = int(input("Digite um número: "))

fib0 = 0
fib1 = 1

while fib1 < num:
    fib = fib0 + fib1

    fib0 = fib1
    fib1 = fib

if fib1 == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
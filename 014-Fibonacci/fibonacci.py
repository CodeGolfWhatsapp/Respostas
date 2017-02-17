def fib(n):return n if n <= 1 else fib(n-1) + fib(n-2);
x=int(input());print(fib(x))
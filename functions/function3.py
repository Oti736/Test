# Exercise 3: Fibonacci up to N

def fibonacci_upto(n):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib

# Example
print(fibonacci_upto(50))  

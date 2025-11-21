# Bazat pe fibonacci.py (Recursivitate cu Memoization)
def fibonacci(n, memo={}):
    """
    Calculează al n-lea număr Fibonacci folosind recursivitatea cu memoization.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    # Folosim memo pentru a stoca rezultatele deja calculate
    if n in memo: 
        return memo[n]
    
    # Cazul de bază
    if n <= 0:
        return 0
    if n == 1: 
        return 1
        
    # Calculează și stochează rezultatul
    memo[n] = fibonacci(n-2, memo) + fibonacci(n-1, memo)
    return memo[n]


def main():
    n = 10
    print(f"Al {n}-lea număr Fibonacci este: {fibonacci(n)}")
    
    # Pentru un N mai mare (ex. 100), memoization este crucială (rezultat bazat pe fișierul original)
    n_large = 100 
    memo_large = {}
    result_large = fibonacci(n_large, memo_large)
    print(f"Al {n_large}-lea număr Fibonacci este: {result_large}")

if __name__ == '__main__':
    main()
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(count):
    sequence = []
    for i in range(count):
        sequence.append(fibonacci_iterative(i))
    return sequence

if __name__ == "__main__":
    n = 10
    print(f"피보나치 수열 첫 {n}개 항:")
    print(fibonacci_sequence(n))
    
    print(f"\n피보나치 수열 10번째 항: {fibonacci_iterative(10)}")
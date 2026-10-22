def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursive(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

# Input number of terms
num_terms = int(input("Enter the number of terms: "))

# Generate and print Fibonacci sequence
print(fibonacci_recursive(num_terms))
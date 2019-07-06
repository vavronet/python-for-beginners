# Make a function that returns the fibonacci sequence for the first n elements.

def fibonacci(n):
    sequence = [0,1]
    while len(sequence) < n:
        sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])
    return sequence


print(fibonacci(8))
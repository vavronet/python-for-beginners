# Write a program that prints the Fibonacci sequence up to 60.
# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 
# The next number is found by adding up the two numbers before it.

fibonacci_seq = [0,1]
previous = 1
before_previous = 0

while previous + before_previous <= 60:
    next_f = previous + before_previous
    fibonacci_seq.append(next_f)
    before_previous = previous
    previous = next_f

print(fibonacci_seq)
def print_fibonacci(length):
    if length == 0:
        return []
    elif length == 1:
        return [0]

    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < length:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence[:length]

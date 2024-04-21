
def print_reverse_pyramid(n):
    for i in range(n, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(' ', end='')
        
        # Print asterisks
        for k in range(2 * i - 1):
            print('*', end='')
        
        # Move to the next line
        print()

# Example usage:
print_reverse_pyramid(5)

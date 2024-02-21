#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Parameters:
    - n (int): The desired number of 'H' characters.

    Returns:
    - int: The minimum number of operations needed.
    If n is impossible to achieve, return 0.
    """

    # Base case: No operations needed for a single 'H'
    if n == 1:
        return 0

    # Initialize an array to store the min. operations for each position
    operations = [float('inf')] * (n + 1)
    operations[1] = 0  # Base case

    # Dynamically fill the operations array
    for i in range(2, n + 1):
        for j in range(1, i):
            # Check if i is divisible by j
            if i % j == 0:
                # Update the min. operations for position i
                operations[i] = min(operations[i], operations[j] + i // j)

    # Return the result if achievable, otherwise return 0
    return operations[n] if operations[n] != float('inf') else 0

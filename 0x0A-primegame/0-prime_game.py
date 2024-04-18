#!/usr/bin/python3
""" Prime Game - A function to find the winner"""


def isWinner(x, nums):
    """
    Determine the winner of each round of the game.

    Args:
    x (int): The number of rounds.
    nums (List[int]): An array of n for each round.

    Returns:
    str or None: The name of the player that won the most rounds.
    If the winner cannot be determined, returns None.

    Constraints:
    - n and x will not be larger than 10000.
    - Cannot import any packages.
    """

    def is_prime(num):
        # Function to check if a number is prime

        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_generator(n):
        # Function to generate prime numbers up to n
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        return primes

    def game_result(n):
        # Function to simulate the game for a given n and return the winner
        primes = prime_generator(n)
        turn = 0  # 0 for Maria, 1 for Ben

        while primes:
            if turn == 0:  # Maria's turn
                for prime in primes:
                    if prime <= n:
                        primes.remove(prime)
                        multiples = [prime * i for i
                                     in range(1, (n // prime) + 1)]
                        primes = [p for p in primes if p not in multiples]
                        turn = 1  # Switch turn to Ben
                        break
                else:
                    return "Ben"
            else:  # Ben's turn
                for prime in primes:
                    if prime <= n:
                        primes.remove(prime)
                        multiples = [prime * i for i
                                     in range(1, (n // prime) + 1)]
                        primes = [p for p in primes if p not in multiples]
                        turn = 0  # Switch turn to Maria
                        break
                else:
                    return "Maria"

        return "Ben" if turn == 0 else "Maria"

    # Play the game for each round and keep track of the winner
    winners = [game_result(n) for n in nums]

    # Count the number of wins for Maria and Ben
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

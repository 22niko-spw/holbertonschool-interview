#!/usr/bin/python3
"""Prime Game module.

Maria and Ben take turns removing a prime and its multiples from a
set of consecutive integers starting at 1. The player who cannot
choose a prime loses. This module determines the overall winner
across several rounds.
"""


def isWinner(x, nums):
    """Determine who wins the most rounds of the Prime Game.

    Args:
        x (int): number of rounds.
        nums (list): list of n values, one per round.

    Returns:
        str: "Maria" or "Ben", whoever won the most rounds.
        None: if there is no clear winner (a tie).
    """
    if not nums or x < 1:
        return None

    n_max = max(nums)
    # Sieve of Eratosthenes up to n_max
    sieve = [True] * (n_max + 1)
    sieve[0] = False
    if n_max >= 1:
        sieve[1] = False

    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n_max + 1, i):
                sieve[multiple] = False

    # prime_count[n] = number of primes <= n
    prime_count = [0] * (n_max + 1)
    count = 0
    for i in range(n_max + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            # No primes available, Ben wins by default
            ben_wins += 1
            continue
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

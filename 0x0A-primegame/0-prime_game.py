#!/usr/bin/python3
""" Prime Game Solution Module """


def isWinner(x, nums):
    """Determine the winner of the prime game based on number of rounds."""
    if not nums or x < 1:
        return None

    # Find the maximum number from the nums list
    limit = max(nums)

    # Create a boolean array to mark prime numbers
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Implement Sieve of Eratosthenes to mark non-prime numbers
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    # Create a cumulative count of prime numbers
    prime_count = [0] * (limit + 1)
    current_count = 0
    for index in range(len(is_prime)):
        if is_prime[index]:
            current_count += 1
        prime_count[index] = current_count

    # Determine how many rounds Maria wins
    maria_wins = 0
    total_rounds = len(nums)

    for number in nums:
        if prime_count[number] % 2 == 1:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins * 2 > total_rounds:
        return "Maria"
    elif maria_wins * 2 == total_rounds:
        return None
    else:
        return "Ben"

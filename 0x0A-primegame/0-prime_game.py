#!/usr/bin/python3
"""
0-prime_game
"""


def isWinner(x, nums):
    """
    Args:
     x - number of rounds.
     nums - list of n's.
     n - set of consecutive integers starting from 1 up to and including n
    Maria plays first and chooses prirme number
    and factors and removed from the list.
    """
    score_dict = {"Maria": 0, "Ben": 0}
    prime_num_list = [0, 0, 2]
    insert_prime(max(nums), prime_num_list)

    for round in range(x):
        _sum = sum(
            (i != 0 and i <= nums[round])
            for i in prime_num_list[: nums[round] + 1]
        )
        if _sum % 2:
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score_dict[winner] += 1

    if score_dict["Maria"] > score_dict["Ben"]:
        return "Maria"
    elif score_dict["Ben"] > score_dict["Maria"]:
        return "Ben"

    return None


def check_prime(n):
    """Check if n is a prime number"""
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True


def insert_prime(n, prime_num_list):
    """Add prime to list"""
    last_prime = prime_num_list[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if check_prime(i):
                prime_num_list.append(i)
            else:
                prime_num_list.append(0)

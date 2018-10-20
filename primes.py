# def is_prime(number):
#     """Return True if *number* is prime."""
#     # if number < 0: #
#     #     return False
#     #
#     # if number in (0, 1):
#     #     return False
#     if number <= 1:
#         return False
#
#     for element in range(2, number):
#         if number % element == 0:
#             return False
#
#     return True

def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False

    """Here refactor for loop"""
    return False if len([False for element in range(2, number) if number % element == 0]) > 0  else True

    # return ( number % element == 0 for element in range(2, number) )
        # return False if number % element == 0 else True
            # return False

    # return True

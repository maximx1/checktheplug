import random
import string

"""
    Generates a random string of alphanumeric characters with length of n (8 by default)
"""
def random_alpha_numeric(n=8):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits)for _ in range(n))
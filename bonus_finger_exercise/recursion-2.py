def is_even(n):
    """ n is an int
    Returns True if n is even and False otherwise """
    # fix this code
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n-2)

print(is_even(5))
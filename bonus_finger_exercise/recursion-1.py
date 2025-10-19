def g(n):
    """ n is an int
    Returns the sum of digits in n """
    # fix this code
    if n == 1:
        return 1
    else:
        return n+g(n-1)

print(g(2))
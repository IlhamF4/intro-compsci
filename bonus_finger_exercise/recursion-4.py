def g(n):
    """ n is an int
    Returns the sum of digits in n """
    # fix this code
    str_n = str(n)
    if len(str_n) == 1:
        return n
    else:
        return int(str_n[0]) + g(int(str_n[1:]))

print(g(443))
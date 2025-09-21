def remove_from_list(L1, L2):
    """ L1 and L2 are lists
    Mutate L1 such that it contains the same elements in the same 
    order, but without any elements that appear in L2. """
    Lnew = L1[:]
    L1.clear()
    for i in range(len(Lnew)):
        if Lnew[i] not in L2:
            L1.append(Lnew[i])

# Examples
L1 = [4,3,6,7,3,2,1,3]
L2 = [1,3]
remove_from_list(L1, L2)
print(L1)   # prints the list [4, 6, 7, 2]
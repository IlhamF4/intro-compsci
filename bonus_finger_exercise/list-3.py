def correct_ordered_sentence(s):
    """ s is a string representing a sentence of the form: 
               noun likes to verb1 verb2 verb3 ... verbn.
        Returns a string of the form:
               noun likes to verb1, verb2, and verb3 .. verbn where the
               verbs are now in alphabetical order.
        Note: noun might be one or many words
    """
    # your code here
    s = s[:-1]
    wordlist = s.split(" ")
    word1 = " ".join([wordlist[i] for i in range(3)])
    word2 = wordlist[3:len(wordlist)]
    word2.sort()
    return word1 + " " + " ".join([i + "," if word2.index(i) != len(word2)-1 else "and " + i for i in word2]) + "."

# Examples    
s = 'ana likes to run skip jump hop dance.'
print(correct_ordered_sentence(s)) 
            # prints ana likes to dance, hop, jump, run, and skip.
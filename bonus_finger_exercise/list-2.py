def correct_sentence(s):
    """ s is a string representing a sentence of the form: 
               noun likes to verb1 verb2 verb3.
        Returns a string of the form:
               noun likes to verb1, verb2, and verb3.
        Note: noun might be one or many words.
    """
    # your code here
    word = ""
    wordlist = s.split(" ")
    return " ".join([word + i if wordlist.index(i) != len(wordlist)-1 else word + "and " + i for i in wordlist ])
    #for i in wordlist:
#    	if wordlist.index(i) == len(wordlist)-1:
#    		word = word + "and "
#    	word = word + i + " "
#    return word
    
# Examples
s = 'ana likes to run skip jump.'
print(correct_sentence(s)) # prints ana likes to run, skip, and jump.
s = 'my mom likes to run skip jump.'
print(correct_sentence(s)) # prints my mom likes to run, skip, and jump.
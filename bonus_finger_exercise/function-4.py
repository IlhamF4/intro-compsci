def count_word(s):
	count = 0
	for i in s:
		if i == '@':
			count += 1
	return count

def validate_address(s):
    """ s is a str
    Returns True if s is a valid email address and False otherwise. 
    A valid email address contains #@#.# where you have one '@' sign but 
    one or more # (any alphabetical or digit character) in each of the 3 places. 
    """
    # your code here
    #check @ symbol
    if '@' not in s or count_word(s) > 1:
    	return False
    
    text1, text2 = s.split('@')
    text3,text4 = text2.split('.')
    if not text1[0].isalnum():
    	return False
    elif not text3.isalnum():
    	return False
    elif not text4.isalnum():
    	return False
    return True

# Examples
print(validate_address('anabell@mit.edu'))           # prints True
print(validate_address('ana.bell@mit.edu'))          # prints True
print(validate_address('a@a.a'))                     # prints True
print(validate_address('anabanana123@hotmail.com'))  # prints True
print(validate_address('a@.edu'))                    # prints False
print(validate_address('***@mit.edu'))               # prints False
print(validate_address('ana@bell@mit.edu'))          # prints False
print(validate_address('anabellmitedu'))             # prints False
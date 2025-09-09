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

def validate_many_addresses(s):
    """ s is a str, supposed to contain many email addresses separated by a space
                    assume the last character in s is an empty space
    
    Returns True if ALL emails addresses in a are valid email addresses and False otherwise. 
    A valid email address contains #@#.# where you have one '@' sign but 
    one or more # (any alphabetical or digit character) in each of the 3 places. 
    """
    # your code here
    wordlist = s.split(' ')
    val = []
    flag = None
    for i in wordlist:
    	if i != "":
    		val.append(validate_address(i))
    if False in val:
    	return False
    else:
    	return True

# Examples
print(validate_many_addresses('a@mit.edu a@a.a '))          # prints True
print(validate_many_addresses('a@a.a b@b.b c@c.c d@d.d '))  # prints True
print(validate_many_addresses('a.b@m.u aa@.bb '))           # prints False
print(validate_many_addresses('be@gm.co aaa@.bb cc#@d.e ')) # prints False
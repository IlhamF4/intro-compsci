def is_in(word1, word2):
	if (word1 in word2) or (word2 in word1):
		return True
	else:
		return False

def test_is_in(words1, words2):
	for a in words1:
		for b in words2:
			result = is_in(a, b)
			if result == False:
				val = False
			else:
				val = True
			print(f'word1 = {a}, words2 = {b}, result = {val}')

words1 = ('hello', 'holila', 'cannot')
words2 = ('indo', 'cannot', 'hell')
test_is_in(words1, words2)
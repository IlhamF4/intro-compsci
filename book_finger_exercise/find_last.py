def find_last(s, sub):
	if s.find(sub) == -1:
		return None
	else:
#		val = s.find(sub)
#		#while True:
#		new_val = s[val + 1::].find(sub)
#		print(s[val+1::].find(sub))
			#if new_val == val:
#				break
#			else:
#				val = new_val
#		return val
		val = s[-1::].find(sub)
		# this is formula to find original position before reverse the word
		return len(s) - len(sub) - val

val = find_last('aca','a')
print(val)
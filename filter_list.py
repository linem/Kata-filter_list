
def filter_list(l):
	for element in l:
		if element not in range(0,10):
			l.remove(element)
	return l

filter_list([1,2,'a','b'])


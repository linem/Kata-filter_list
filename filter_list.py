
def filter_list(l):
	for element in l:
		if element not in range(0,10):
			l.remove(element)
	return l

filter_list([1,2,'a','b'])
#The list becomes shorter every time you take out something from the list. 
#I guess that alters the behavior of the for loop. 
#In this case you could probably work around it. But I would create another list and add the number elements to them.


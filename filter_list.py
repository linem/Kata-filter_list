
def filter_list(l):
	new_list = []
	for element in l:
		if type(element) == int:
			new_list.append(element)
	return new_list

filter_list([1,2,'a','b'])
#The list becomes shorter every time you take out something from the list. 
#I guess that alters the behavior of the for loop. 
#In this case you could probably work around it. But I would create another list and add the number elements to them.

#Updated:
#New list added for appending
#And bug fixed, as numbers could be higher than 10.


# input is a list and a number to search in that list
# output index if number is in list otherwise, item not found

def seq_search(lst, item):
	index = 0
	found = False
	while index < len(lst) and not found:
		if lst[index] == item:
			found = True
		else:
			index += 1
			
	return found
	
lst = [1,2,3,4,5,6,7,8,9]
print(seq_search(lst, 5))
print(seq_search(lst, 10))
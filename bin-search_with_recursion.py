# input - a list and an item to find
# output- if item exists True else False
# input list should be sorted

def bin_search(aList, item):
	first = 0
	last = len(aList)-1
	
	mid = (first + last) // 2
	if len(aList) == 0:
		return False
	else:
		if aList[mid] == item:
			return True
		elif aList[mid] < item:
			return bin_search(aList[mid+1:], item)
		else:
			return bin_search(aList[:mid], item)
	
	
	
aList = [0,1,2,3,4,4,5,6,7]
print(bin_search(aList, 4))
print(bin_search(aList, 9))
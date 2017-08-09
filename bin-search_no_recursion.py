# input - a list and an item to find
# output- if item exists True else False
# input list should be sorted

def bin_search(aList, item):
	first = 0
	last = len(aList)-1
	stop = False
	
	while (first <= last) and not stop:
		mid = (first + last) // 2
		if aList[mid] == item:
			stop = True
		elif aList[mid] < item:
			first = mid + 1
		else:
			last = mid - 1
	
	return stop
	
aList = [0,1,2,3,4,4,5,6]
print(bin_search(aList, 5))
print(bin_search(aList, 7))
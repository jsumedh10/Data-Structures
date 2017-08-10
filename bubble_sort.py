def bubble_sort(aList):
	
	for i in range(len(aList)-1, 0, -1):
		for j in range(i):
			if aList[j] > aList[j+1]:
				aList[j], aList[j+1] = aList[j+1], aList[j]
			
				
aList = [6,5,4,3,2,1]
bubble_sort(aList)
print(aList)


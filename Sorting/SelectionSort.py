A = [5,4,3,2,1]


def selectionSort(A):
	
	for i in range(len(A)):
		indexOfMin = i
		for j in range(i+1,len(A)):
			if A[i]>A[j]:
				indexOfMin = j
		A[i],A[indexOfMin]=A[indexOfMin],A[i]
	
	return A
	
print(selectionSort(A))
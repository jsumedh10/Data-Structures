#bubble sort
#compare adjacent elements
#if previous number is bigger swap it with smaller number
#at every pass, largest number will reach the end
A=[5,4,3,2,1]

def bubbleSort(A):
	for i in range(len(A)-1,0,-1):
		for j in range(i):
			if A[j]>A[j+1]:
				A[j],A[j+1]=A[j+1],A[j]
				
	return A

print(bubbleSort(A))
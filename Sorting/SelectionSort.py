# author: Sumedh Junghare
A = [5,4,3,2,1]
#A=[3,2,1,4]

#select minimum number
#put it at the start
#when the first minimum number reaches 0th place,
#all other minimum numbers follow that number

def selectionSort(A):
	
	for i in range(len(A)):
		indexOfMin = i
		for j in range(i+1,len(A)):
			if A[i]>A[j]:
				indexOfMin = j
		A[i],A[indexOfMin]=A[indexOfMin],A[i]
		#print("PASS: "+str(i)+" "+str(A) )
	
	return A
	
print(selectionSort(A))
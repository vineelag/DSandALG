#Insertion Sort 

def insertion_sort(A):
    for i in range(1, len(A)): #outer loop
        for j in range(i-1, -1, -1): #-1 since we will move towards    left in the loop
            if A[j] > A[j+1]:
               A[j], A[j+1] = A[j+1], A[j] #swaping values
             else:
                break

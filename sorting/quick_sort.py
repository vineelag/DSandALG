def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
   if low < hi:
      p = partition(A, low, hi)
      quick_sort2(A, low, p-1)
      quick_sort2(A, p+1, hi)

def get_pivot(A, low, hi):
    mid = (hi + low) // 2
   pivot = hi
   if A[low] < A[mid]:
     if A[mid] < A[hi]:
        pivot = mid
   elif A[low] < A[hi]:
        pivot = low
    return pivot

def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
  A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

for i in range(low, hi+1):
   if A[i] < pivotValue:
     border += 1
    A[i], A[border] = A[border], A[i]
   A[low], A[border] = A[border], A[low]

  return (border)

def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]

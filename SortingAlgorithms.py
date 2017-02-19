def mergesort(array):

	def merge(array1, array2):
		result = []

		index1 = 0
		index2 = 0

		while index1 < len(array1) and index2 < len(array2):
			if array1[index1] < array2[index2]:
				result.append(array1[index1])
				index1 += 1
			else:
				result.append(array2[index2])
				index2 += 1

		while index1 < len(array1):
			result.append(array1[index1])
			index1 += 1
		while index2 < len(array2):
			result.append(array2[index2])
			index2 += 1

		return result

	if len(array) <= 1:
		return array
	else:
		left = mergesort(array[0:len(array)/2])
		right = mergesort(array[len(array)/2:len(array)])
		return merge(left, right)

def quicksort(array):

	def partition(array, start, end):

		def swap(array, index1, index2):
			temp = array[index1]
			array[index1] = array[index2]
			array[index2] = temp

		pivotIndex = start

		left = start + 1
		right = end - 1

		while(left < right):
			while(left < len(array) and array[left] < array[pivotIndex] and left < right):
				left += 1
			while(right >= 0 and array[right] >= array[pivotIndex] and left < right):
				right -= 1

			if left < right:
				swap(array, left, right)
				left += 1
				right -= 1

		if array[left] < array[pivotIndex]:
			swap(array, pivotIndex, left)
			return left
		else:
			swap(array, pivotIndex, left - 1)
			return left - 1


	def quicksortHelper(array, start, end):
		if end - start <= 1:
			return array
		else:
			middle = partition(array, start, end)

			if(middle - start > 0):
				quicksortHelper(array, start, middle)
			if(end - (middle + 1) > 0):
				quicksortHelper(array, middle + 1, end)

	quicksortHelper(array, 0, len(array))
	return array

def testMergesort():
	pass

def main():
	array = [1, -5, 4, 10, 6, 2, 7, -1, -245]
	array = [-111, -12121212, 23, 7,3,2,2,4,6,7,8,6,4,3]

	print quicksort(array)
	print mergesort(array)

main()
import hashlib

class MyHashTable:

	class Entry:
		def __init__(self, key, value):
			self.key = key
			self.value = value

	def __init__(self):
		self.SIZE = 100
		self.array = [None] * 100

	def _getHashCode(self, key):
		return int(hashlib.md5(str(key)).hexdigest(), 16) % self.SIZE

	def put(self, key, value):
		index = self._getHashCode(key)

		# If the hash array contains an entry in this index
		if self.array[index] is not None:
			for entry in self.array[index]:
				if entry.key == key:
					entry.value = value
					return

			newEntry = self.Entry(key, value)
			self.array.append(newEntry)
		else:
			newEntry = self.Entry(key, value)
			self.array[index] = [newEntry]

	def get(self, key):
		index = self._getHashCode(key)
		
		if self.array[index] is not None:
			for entry in self.array[index]:
				if entry.key == key:
					return entry.value

		return None

	def remove(self, key):
		index = self._getHashCode(key)
		
		if self.array[index] is not None:
			for i in range(0, len(self.array[index])):
				entry = self.array[index][i]
				if entry.key == key:
					del self.array[index]

		return None

	def hasKey(self, key):
		index = self._getHashCode(key)
		
		if self.array[index] is not None:
			for entry in self.array[index]:
				if entry.key == key:
					return True

		return False



def main():
	map = MyHashTable()

	map.put(1, 2)
	assert(map.get(1) == 2)

	map.put(1, 3)
	assert(map.get(1) == 3)

	map.put(3, 4)
	assert(map.get(3) == 4)

	assert(map.hasKey(1) == True)
	assert(map.hasKey(3) == True)
	assert(map.hasKey(9) == False)

	map.put(7, 8)
	assert(map.hasKey(7) == True)
	map.remove(7)
	assert(map.hasKey(7) == False)
	map.remove(7)
	assert(map.hasKey(7) == False)

main()
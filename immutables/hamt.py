#!/usr/bin/env python

"""

Hashed Array Mapped Trie

Implementation based on the paper "Ideal Hash Trees" by Phil Bagwell.

"""

__author__ = "Alexandru Marinescu"
__contact__ = "almarinescu@gmail.com"

class BitmapHashTable(object):
	def __init__(self, bitmap=0, values=[]):
		self.bitmap = bitmap
		self.values = values

	def _idx(self, key):
		"""
		Compute the index in the value list for a given key.
		
		The index is computed by counting the number of 1s in the bitmap below the
		bit given by the `key` argument.
		"""
		if key > 0:
			return hammingWeight(lastNBits(self.bitmap, key))

		return 0

	def insert(self, key, value):
		if self.hasKey(key):
			self.values[self._idx(key)] = value
		else:
			self.bitmap = setBitAt(self.bitmap, key)
			self.values = self._insertValue(key, value)

	def _insertValue(self, key, value):
		return self.values[0:self._idx(key)] + [value] + self.values[self._idx(key):]

	def delete(self, key):
		self.values = self._removeValue(key)
		self.bitmap = unsetBitAt(self.bitmap, key)

	def _removeValue(self, key):
		if self.hasKey(key):
			remIdx = self._idx(key)
			if remIdx == 0:
				if len(self.values) > 1:
					return self.values[1:]
				else:
					return []
			else:
				newValues = self.values[0:remIdx]
				if remIdx+1 != len(self.values):
					newValues += self.values[remIdx+1:]

				return newValues
		else:
			return self.values

	def hasKey(self, key):
		return isBitSet(self.bitmap, key)

	def get(self, key):
		if not self.hasKey(key):
			return None
		else:
			return self.values[self._idx(key)]
	
	def __len__(self):
		return hammingWeight(self.bitmap)

class ImmutableBitmapHashTable(BitmapHashTable):
	pass

class Hamt(object):
	""" Array Mapped Trie """
	def __init__(self):
		self.table = BitmapHashTable()

	def insert(self, key, value):
		pass

	def contains(self, key):
		"""Check if the hash table contains the given key."""
		return self.get(key) is not None

	def get(self, key):
		hashedKey = hash(key)
		node = self
		level = 0
		numLevels = 32 // 5

		while level <= numLevels:
			# Get the bits corresponding to the current level in the hashed key.
			tableKey = getBitsAtLevel(hashedKey, level)

			# Check if the table contains the given index.
			if not node.table.hasKey(tableKey):
				return None
			else:
				node = self.table.get(tableKey)
				level += 1

				if isinstance(tuple, entry):
					if node[0] == key:
						return node[1]
					else:
						return None

		# We failed to find the given key.
		return None

	def delete(self, key):
		pass

m1 = 0x55555555
m2 = 0x33333333
m4 = 0x0f0f0f0f

def hammingWeight(x):
	"""Compute the Hamming weight (the number of non-zero bits)."""
	x = abs(x)

	x -= (x >> 1) & m1
	x = (x & m2) + ((x >> 2) & m2)
	x = (x + (x >> 4)) & m4
	x += x >>  8
	x += x >> 16
	x += x >> 32

	return x & 0x7f

def getBitsAtLevel(n, level):
	return (n >> (5 * level)) & 0x1f

def isBitSet(value, index):
	return ((1 << index) & value) != 0

def setBitAt(value, index):
	return (1 << index) ^ value

def unsetBitAt(value, index):
	return ~(1 << index) & value

def lastNBits(value, nbits):
	if nbits == 0:
		return 0
	return value & int('1' * nbits, 2)

def bitsBelow(value, index):
	shift = 1 << index
	return (shift | ~shift) & value

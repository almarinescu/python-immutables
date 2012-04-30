#!/usr/bin/env python

"""

Hashed Array Mapped Trie

Implementation based on the paper "Ideal Hash Trees" by Phil Bagwell.

"""

__author__ = "Alexandru Marinescu"
__contact__ = "almarinescu@gmail.com"

class Amt(object):
	""" Array Mapped Trie """
	def __init__(self):
		self.root = (0, [])

	@property
	def bitmap(self):
		return self.root[0]

	@property
	def values(self):
		return self.root[1]

	def insert(self, key, value):
		pass

	def contains(self, key):
		"""Check if the hash table contains the given key."""
		return self.search(key) is not None

	def search(self, key):
		hashedKey = hash(key)
		node = self
		level = 0
		numLevels = 32 // 5

		while level <= numLevels:
			tableIndex = getBitsAtLevel(hashedKey, level)

			# Check if the table contains the given index.
			if not isBitSet(node.bitmap, tableIndex):
				return None
			else:
				bitmapIndex = hammingWeight(lastNBits(node.bitmap, tableIndex))

				# If the node has at the given index a tuple:
				if isinstance(node.values[bitmapIndex], tuple):
					# Check if the key matches.
					if node.values[bitmapIndex][0] == key:
						return node.values[bitmapIndex][1]
					else:
						return None
				# We must go into the next level.
				else:
					node = node.values[bitmapIndex]
					level += 1

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
	return value & int('1' * nbits, 2)

def bitsBelow(value, index):
	shift = 1 << index
	return (shift | ~shift) & value

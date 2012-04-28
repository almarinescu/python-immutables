#!/usr/bin/env python

"""

Array Mapped Trie

Implementation based on the paper "Ideal Hash Trees" by Phil Bagwell.

"""

__author__ = "Alexandru Marinescu"
__contact__ = "almarinescu@gmail.com"

class BitmapHash(object):
	def __init__(self):
		self.bitmap = 0
		self.values = []

	def search(self, key):
		if isBitSet(self.bitmap, key):
			return self.values[hammingWeight()]

	def insert(self, key, value):
		pass

	def delete(self, key, value):
		pass

class Amt(object):
	""" Array Mapped Trie """

	def __init__(self):
		self.root = None

	def insert(self, key, value):
		pass
	
	def search(self, key):
		return self._find_key(self.root, hash(key), key, 0)

	def _find_key(self, root, key_hash, key, level):
		if root is None:
			return None
		
		if isinstance(root, tuple):
			if root[0] == key:
				return root[1]
			else:
				return None
		else:
			bits = getBitsAtLevel(level)
			return self._find_key(root[bits], key_hash, key, level+1)

	def delete(self, key):
		pass

class ImmutableList(Amt):
	pass

class ImmutableDict(Amt):
	pass

class ImmutableSet(Amt):
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

def bitsBelow(value, index):
	shift = 1 << index
	return (shift | ~shift) & value

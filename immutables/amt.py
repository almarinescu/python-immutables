#!/usr/bin/env python

"""
Array Mapped Trie

Implementation based on the paper "Ideal Hash Trees" by Phil Bagwell.
"""

__author__ = "Alexandru Marinescu"
__contact__ = "almarinescu@gmail.com"

class AmtNode(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value

class Amt(object):
	"""
	Array Mapped Trie

	"""
	def __init__(self):
		pass

	def insert(self, key, value):
		pass
	
	def search(self, key):
		pass

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

	x -= (x >> 1) & m1
	x = (x & m2) + ((x >> 2) & m2)
	x = (x + (x >> 4)) & m4
	x += x >>  8
	x += x >> 16
	x += x >> 32

	return x & 0x7f

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

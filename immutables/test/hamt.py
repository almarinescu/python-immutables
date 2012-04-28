#!/usr/bin/env python

import unittest

from immutables import hamt

__author__ = "Alexandru Marinescu"
__contact__ = "almarinescu@gmail.com"

class TestAmt(unittest.TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass

	def testInsert(self):
		pass

	def testSearch(self):
		pass

	def testDelete(self):
		pass

	def testHammingWeight(self):
		self.assertEquals(0, hamt.hammingWeight(0))
		self.assertEquals(1, hamt.hammingWeight(8))
		self.assertEquals(4, hamt.hammingWeight(15))
		self.assertEquals(7, hamt.hammingWeight(127))
		self.assertEquals(8, hamt.hammingWeight(255))
		self.assertEquals(8, hamt.hammingWeight(198561))

	def testHamtBitmapOperations(self):
		pass

if __name__ == '__main__':
	unittest.main()

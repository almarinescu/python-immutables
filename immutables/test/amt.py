#!/usr/bin/env python

import unittest

from immutables import amt

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
		self.assertEquals(0, amt.hammingWeight(0))
		self.assertEquals(1, amt.hammingWeight(8))
		self.assertEquals(4, amt.hammingWeight(15))
		self.assertEquals(7, amt.hammingWeight(127))
		self.assertEquals(8, amt.hammingWeight(255))
		self.assertEquals(8, amt.hammingWeight(198561))

if __name__ == '__main__':
	unittest.main()

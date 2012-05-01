#!/usr/bin/env python

import unittest

from immutables import hamt

__author__ = "Alexandru Marinescu"
__contact__ = "almarinescu@gmail.com"

class TestBitmapHashTable(unittest.TestCase):
	def testInsert(self):
		bht = hamt.BitmapHashTable()
		bht.insert(0, 1000)
		self.assertEquals(bht.get(0), 1000)

		bht.insert(1, {})
		self.assertEquals(bht.get(1), {})

		bht.insert(10, "ana")
		self.assertEquals(bht.get(10), 'ana')

		bht.delete(1)
		self.assertEquals(len(bht), 2) 

		for i in xrange(10):
			bht.insert(i, i*2)

		for i in xrange(10):
			self.assertEquals(bht.get(i), i*2)

		bht = hamt.BitmapHashTable()
		bht.insert(100, '100-val')
		bht.insert(2, '2-val')

		self.assertEquals(bht.get(100), '100-val')
		self.assertEquals(bht.get(2), '2-val')

		print bht.values
		print bin(bht.bitmap)

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

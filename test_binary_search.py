import unittest
import unittest.mock
import binary_search
import sys
import io
from unittest import mock
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    def __int__(self):
    	pass

    def setUp(self):
    	self._list1 = list(range(1,101))
    	self._list2 = [1,5,25,100,42,300,5,0,500]
    	self._item1 = 75
    	self._item2 = 51
    	self._item3 = 25
    	self._item4 = 1
    	self._item5 = 100
    	self._item6 = 50

    @patch("binary_search.binary_test_high")
    def test_high_value(self, mock_high_test):
    	text_trap = io.StringIO()
    	sys.stdout = text_trap
    	binary_search.binary_search(self._list1, self._item1)
    	self.assertTrue(mock_high_test)

    @patch("binary_search.binary_test_low")
    def test_low_value(self, mock_low_test):
    	text_trap = io.StringIO()
    	sys.stdout = text_trap
    	binary_search.binary_search(self._list1, self._item3)
    	self.assertTrue(mock_low_test)

    def test_binary_search(self):
    	text_trap = io.StringIO()
    	sys.stdout = text_trap
    	self.assertEqual(binary_search.binary_search(self._list1, self._item2),51)

    def test_low_return(self):
    	text_trap = io.StringIO()
    	sys.stdout = text_trap
    	self.assertEqual(binary_search.binary_test_low(self._list1, self._item6),list(range(51,101)))

    def test_high_return(self):
    	text_trap = io.StringIO()
    	sys.stdout = text_trap
    	self.assertEqual(binary_search.binary_test_high(self._list1, self._item6),list(range(1,51)))

    def test_determine_mid(self):
    	text_trap = io.StringIO()
    	sys.stdout = text_trap
    	self.assertEqual(binary_search.determine_mid(self._list1),50)

if __name__ == '__main__':
    unittest.main()

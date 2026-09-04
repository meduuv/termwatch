import unittest
from termwatch import changed
class Tests(unittest.TestCase):
 def test_changed(self): self.assertFalse(changed('a\n','a\r\n')); self.assertTrue(changed('a','b'))
if __name__=='__main__': unittest.main()

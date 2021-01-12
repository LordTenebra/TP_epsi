# -*- coding: utf-8 -*-
#!/usr/bin/python
import unittest
import reduc
import calc

class Testing(unittest.TestCase):
    def test_int(self):
        b = reduc.prix(900);
        self.assertNotEqual(0, b)


if __name__ == '__main__':
    unittest.main()

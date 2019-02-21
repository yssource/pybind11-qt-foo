# -*- coding: utf-8 -*-

import unittest
import libfoo as foo

class MathTest(unittest.TestCase):
    def testFoo2(self):
        print(foo.foo2())
        self.assertEqual(foo.add(5, 5), 10)

if __name__ == '__main__':
    unittest.main()

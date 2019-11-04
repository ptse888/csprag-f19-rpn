import unittest
import rpn

class TestBasics(unittest.TestCase):
   def test_add(self):
      result = rpn.calculate('1 1 +')
      self.assertEqual(2, result)
   def test_sub(self):
      result = rpn.calculate(5 3 -)
      self.asserEqual(2, result)
   def test_badinput(self):
      with self.aserRaises(TypeError):
         rpn.calculate('1 2 3 +')

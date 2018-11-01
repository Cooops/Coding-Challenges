# https://www.codewars.com/kata/data-reverse/train/python

"""
A stream of data is received and needs to be reversed. Each segment is 8 bits long, meaning the order of these segments need to be reversed, for example:

11111111  00000000  00001111  10101010
  byte1     byte2     byte3     byte4
should become:

10101010  00001111  00000000  11111111
  byte4     byte3     byte2     byte1
The total number of bits will always be a multiple of 8. The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
"""

# MY SOLUTION
def data_reverse(data):
    composite_list = [data[x:x+8] for x in range(0, len(data), 8)]
    reversed_list = list(i for i in reversed(composite_list))
    return [j for i in reversed_list for j in i]

data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

import unittest
class MyTest(unittest.TestCase):
    def test(self, data1, data2):
        self.assertEquals(data_reverse(data1),data2)

MyTest().test(data1, data2)

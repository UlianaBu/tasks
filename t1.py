# -*- coding: utf-8 -*-
"""t1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RlfHLrJJ6VVE-27yMsy9eoDq9B8XAxrm
"""

print ("Введите четыре целых числа: ")
a,b,c,d = int(input()),int(input()),int(input()),int(input())
def min4(a,b,c,d):
  k = min(a,b)
  k1 = min(k,c)
  k2 = min(k1,d)
  return k2
print ("Минимальное число: ", min4(a,b,c,d))
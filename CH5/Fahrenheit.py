#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

def change(fahrenheit) :
  celsuis = (fahrenheit - 32) * (5 / 9)
  return celsuis


if __name__ == '__main__':
  fahrenheit = raw_input("Enter a fahrenheit > ")
  celsuis = change(int(fahrenheit))
  print celsuis


















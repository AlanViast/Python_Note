#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def taxrate(wage) :
  """ Calculation of income tax """
  return (wage - 3500) * 0.05


if __name__ == '__main__':
  wage = raw_input("Enter your wage > ")
  print taxrate(int(wage))

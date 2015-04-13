#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def getSquareArea(edge) :
  return edge ** 2;


def getSquareVolume(edge) :
  return edge ** 3;


if __name__ == '__main__':
  edge = raw_input("Enter a square edge > ")

  print "area: %d" %(getSquareArea(int(edge)))
  print "volume: %d" %(getSquareVolume(int(edge)))






















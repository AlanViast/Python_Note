#!/usr/bin/env python
# -*- coding: UTF-8 -*-

PI = 3.1415926

def getRoundArea(diameter) :
  """ get round area """
  radius = diameter / 2
  area = PI * (radius ** 2)
  return area


def getRoundVolume(diameter) :
  """ get round volume """
  radius = diameter / 2
  volume = (4.18879 * (radius ** 3))
  return volume



if __name__ == '__main__':
  diameter = raw_input("Enter a round diameter > ")

  print "Area: %s" %getRoundArea(float(diameter))
  print "Volume: %s" %getRoundVolume(float(diameter))























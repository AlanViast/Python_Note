#!/usr/bin/env python
# -*- coding: UTF-8 -*-
coinList = [25, 10, 5, 1]

def minCoin(money) :
  if isinstance(money, float) :
    iMoney = int( float( money ) * 100 )
    count = 0
    statisticsCoin = []
    tempMoney = iMoney
    for i in coinList :
      tempCount,tempMoney = divmod(tempMoney, i);
      statisticsCoin.append(tempCount)
    print "%d 可以更换: %d 个25美分, %d个10美分, %d个5美分, %d个1美分" %(iMoney, statisticsCoin[0], statisticsCoin[1], statisticsCoin[2], statisticsCoin[3])

if __name__ == '__main__':
  money = raw_input("Enter money > ")
  minCoin(float(money))

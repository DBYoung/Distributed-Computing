#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#reducer返回mapper三个变量的均值、最大值、方差
#即返回mean1 mean2 mean3 max1 max2 max3 var1 var2 var3 & totalNum

import sys

def read_input(file):
    for line in file:
        yield line.strip()

input = read_input(sys.stdin)

mapperOut = [line.split("\t") for line in input]

cumVal1 = cumVal2 = cumVal3 = 0.0
cumSumSq1 = cumSumSq2 = cumSumSq3 = 0.0
cumN = 0.0

for instance in mapperOut:
    #行数，也就是样本量
    cumN += float(instance[0])
    #三列的总和
    cumVal1 += float(instance[1])
    cumVal2 += float(instance[2])
    cumVal3 += float(instance[3])
    #三列的平方和
    cumSumSq1 += float(instance[4])
    cumSumSq2 += float(instance[5])
    cumSumSq3 += float(instance[6])
#三列的均值
mean1 = cumVal1 / cumN
mean2 = cumVal2 / cumN
mean3 = cumVal3 / cumN


#定义一个获取最大值的函数
def getMax(nestList):
    #嵌套列表的每个元素的长度相同
    outlength = len(nestList)
    innerLength = len(nestList[0])
    maxVal = nestList[0]
    for i in range(outlength):
        for j in range(innerLength):
            if nestList[i][j] > maxVal[j]:
                maxVal[j] = nestList[i][j]
    return maxVal

maxVals = []
for i in range(len(mapperOut)):
    maxVals.append([mapperOut[i][7],mapperOut[i][8],mapperOut[i][9]])

maxVals = getMax(maxVals)

#三列的最大值
max1 = float(maxVals[0])
max2 = float(maxVals[1])
max3 = float(maxVals[2])

#三列值的方差
var1 = cumSumSq1 / cumN - mean1 * mean1
var2 = cumSumSq2 / cumN - mean2 * mean2
var3 = cumSumSq3 / cumN - mean3 * mean3
print "-------------------------------------------------------------------------------"
print "Observations:%d\nmeans of three columns:%f\t%f\t%f\nmax values of three columns:%f\t%f\t%f\ndeviations of three columns:%f\t%f\t%f"  \
%(cumN,mean1,mean2,mean3,max1,max2,max3,var1,var2,var3)
print "-------------------------------------------------------------------------------"
#print mapperOut[0]

#print len(mapperOut[0])


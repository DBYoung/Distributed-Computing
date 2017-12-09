#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
def read_input(file):
    for line in file:
        yield line.strip()

input = read_input(sys.stdin)
data = []
for line in input:
    line = line.split(",")
    a = float(line[1])
    b = float(line[2])
    c = float(line[3])
    data.append([a,b,c])
numInput = len(data)
cumSum = cumSumSq = [0.0,0.0,0.0]

#以下循环实现所有变量值的求和，均值部分不在此实现
for i in range(numInput):
    cumSum = map(lambda x,y:x+y,cumSum,data[i])
    cumSumSq = map(lambda x,y:x+y*y,cumSumSq,data[i])
#下面计算平方和数据
#cumSumSq = [0.0,0.0,0.0]
#for i in range(numInput):
#    cunSumSq = map(lambda x,y:x+y*y,cumSumSq,data[i])

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
#计算最大值
maxVal = getMax(data)
#输出的结果为：数值个数 三个列的和 三个列的平方和 三个列的最大值
print "%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f" %(numInput,cumSum[0],cumSum[1],cumSum[2],cumSumSq[0],cumSumSq[1],cumSumSq[2],maxVal[0],maxVal[1],maxVal[2])
sys.stdin.close()

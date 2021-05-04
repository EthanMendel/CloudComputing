# linreg.py
#
# Standalone Python/Spark program to perform linear regression.
# Performs linear regression by computing the summation form of the
# closed form expression for the ordinary least squares estimate of beta.
# 
# TODO: Write this.
# 
# Takes the yx file as input, where on each line y is the first element 
# and the remaining elements constitute the x.
#
# Usage: spark-submit linreg.py <inputdatafile>
# Example usage: spark-submit linreg.py yxlin.csv
#
#

import sys
import numpy as np

from pyspark import SparkContext
from operator import add

# a=[]
# b=[]
# def getNumA(n):
#   global a
#   a.append(float(n))
#   return True
# def getNumB(n):
#   global b
#   b.append(float(n))

if __name__ == "__main__":
  # global a,b
  # a=[]
  # b=[]
  if len(sys.argv) !=2:
    print >> sys.stderr, "Usage: linreg <datafile>"
    exit(-1)

  sc = SparkContext(appName="LinearRegression")

  # Input yx file has y_i as the first element of each line 
  # and the remaining elements constitute x_i
  yxinputFile = sc.textFile(sys.argv[1])

  yxlines = yxinputFile.map(lambda line: line.split(','))
  yxfirstline = yxlines.first()
  yxlength = len(yxfirstline)
  #print "yxlength: ", yxlength

  # dummy floating point array for beta to illustrate desired output format
  beta = np.zeros(yxlength, dtype=float)

  #
  # Add your code here to compute the array of 
  # linear regression coefficients beta.
  # You may also modify the above code.
  #
#-----------------------------------------------------My Way
  # print("yxlines: %s" % yxlines)
  # print("yxfirstline %s" % yxfirstline)
  pairs=yxlines.take(yxlines.count())#Get Data into array to use
  x=[]
  y=[]
  # print("pairs %s" % pairs)
  for i in range(len(pairs)):#get data into x list and y list
    y.append(float(pairs[i][0]))
    x.append(float(pairs[i][1]))
  a=map(lambda x: x*x,x)#x_subI * x_subI
  #print("Origional A: %s" % a)
  asum=0
  for i in a:#sum of all i (x_subI * x_subI)
    asum+=i
  print("Sum A: %s" % asum)
  b=map(lambda x,y: x*y,x,y)#x_subI * y_subI)
  #print("B: %s" % b)
  bsum=0
  for i in b:#sum of all i (x_subI * y_subI)
    bsum+=i
  print("Sum B: %s" % bsum)
#-----------------------------------------------------PDF way
  # amap=map(lambda x:x*x,x)
  # a=sc.parallelize(amap).reduceByKey(lambda x,y: x+y).collect()
  # bmap=yxlines.map(lambda x,y:x*y).reduceByKey(lambda x,y:x+y).collect()
  # print("A: %s" % a)
  # print("A: %s" % a)
  # print("B: %s" % bmap)
  # print("B: %s" % b)
  # for i in range(len(a)):
  #   a[i]=float(a[i])
  #   b[i]=float(a[i])

  aT=np.matrix(asum).transpose()#transpose A
  b=np.matrix(bsum)
  beta=aT*b#get beta

  # print the linear regression coefficients in desired output format
  print "beta: "
  for coeff in beta:
      print coeff

  sc.stop()
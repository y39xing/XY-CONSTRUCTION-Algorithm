import numpy as np

def setup(nodenum):
  matr=np.full([2,nodenum+1],0)
  for i in range (0,nodenum+1):
    matr[0,i]=i
  return matr

def findpath(matr,n):
  result=[n]
  index=n
  while(1):
    index=matr[1,index]
    if(index==0):
      break
    result.append(index)
  return result

def find(matr,n):
  return matr[1,n]

def update(matr,n,x):
  matr[1,n]=x

def display(matr):
  print(matr[0:2,1:len(matr[0])])





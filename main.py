# This module is an implement of XY-construction algorithm which provides a
# constructive proof of Konig's theoreom

# The input should be a modifed adjacency matrix with a given starting matching
# The input G should be bipartite with bipartition A and B(set)

# The assumption is that G is not directional and there are not any loops and
# Multiple edges
import methods as mt
import numpy as np

def init(v):
# Initialize G given v vertices
    G = np.full([v+1,v+1],0)
    for i in range(1,v+1):
      G[0,i] = i
      G[i,0] = i
    return G

def size(G):
# return the number of vertices in G
    V = len(G) - 1
    return V

def unsat_v(G,n):
# determine if vertex n is unsat in current g
    for i in range(1,size(G)+1):
        if G[n,i] == -1:
            return False
    return True

def unsat(G):
# Find all unsaturated vertex in G
    L = []
    for i in range(1,size(G)+1):
        if (unsat_v(G,i)):
            L.append(i)
    return L

def add_edge(G,m,n,A,B):
# Add common edge in G from m to n
    B1 = np.isin(m,A)
    B2 = np.isin(n,A)
    if (B1 == B2):
        print("Invalid: m, n same bipartition")
        return None
    else:
        if (G[m,n] == -1):
            print("Invalid: mn already matching edges")
        else:
            G[m,n] = 1
            G[n,m] = 1  

def add_matching_edge(G,m,n,A,B):
# Add common edge in G from m to n
    B1 = np.isin(m,A)
    B2 = np.isin(n,A)
    if (B1 == B2):
        print("Invalid: m, n same bipartition")
        return None
    elif ((unsat_v(G,m) * unsat_v(G,n)) == 0):
        print("Invalid: vertex already saturated")
    else:
        G[m,n] = -1
        G[n,m] = -1  

def disp(G):
# Display 1-indexed version of G, without title
    v = size(G)
    print(G[1:v+1,1:v+1])

def status(G,m,n):
# Return the edge status bewtween vertex m and n in graph G
    return G[m,n]
    
def flip(G,m,n):
# Flip the edge status btw vertex m and n in graph G
    G[m,n] = (-1) * G[m,n]
    G[n,m] = (-1) * G[n,m]
    return G[m,n]

def N(G,n,Mode):
# Return the neighbourhood of vertex n
# Mode -1: via matching edges
# Mode 1: via nonmatching edges
    par = Mode
    L = []
    for i in range(1,size(G)+1):
        if (G[n,i] == par):
            L.append(i)
            if (Mode == 0):
                break
    return L
    

def XY_construction(G,A,B):
# Start from bipartition A in default setting
    tree = mt.setup(size(G))
    Unsat_A = np.intersect1d(unsat(G),A)
    Unsat_B = np.intersect1d(unsat(G),B)
    Stop = []
    X = Unsat_A
    Y = []
    XT = list(Unsat_A)
    YT =[]
    count = 1
    while 1:
      #print("XT=",XT)
      for i in range(0,len(XT)):
        Neighbour = N(G,XT[i],count)
        for j in range(0,len(Neighbour)):
          if count == 1:
            if (not Neighbour[j] in Y):
                mt.update(tree,Neighbour[j],XT[i])
                YT.append(Neighbour[j])
          else:
            if (not Neighbour[j] in X):
                mt.update(tree,Neighbour[j],XT[i])
                YT.append(Neighbour[j])
      #print(YT)
      #Stopping Criterion---------------
      Stop = np.intersect1d(Unsat_B,YT)
      #print("Stop=", Stop)
      if (len(Stop) != 0):
        #print(tree)
        return mt.findpath(tree,Stop[0])
      #-----------------------------------
      YT = list(set(YT))
      #print("YT=",YT)
      '''
      if count == 1:
        YT = list(set(YT) - set(X))
      else:
        YT = list(set(YT) - set(Y))
      '''
      for i in range(0,len(YT)):
        if count == 1:
          Y.append(YT[i])
        else:
          X.append(YT[i])
      X = list(set(X))
      Y = list(set(Y))
      #print("X=",X)
      #print("Y=",Y)
      if (len(Y) == 0):
        print("Optimal Result:")
        return None
      XT = YT
      YT = []
      count = count * (-1)
    return None

def perfect_matching(G,A,B):
  temp = G
  while (1):
    aug_path = XY_construction(temp,A,B)
    print("Augmenting path:",aug_path)
    if (aug_path == None):
      break  
    for i in range(0,len(aug_path)-1):
      flip(temp,aug_path[i],aug_path[i+1])
    #print(temp)
  return temp
  
def main():
  G = init(16)
  A = [1,2,3,4,5,6,7,8]
  B = [9,10,11,12,13,14,15,16]
  add_matching_edge(G,1,9,A,B)
  add_edge(G,1,10,A,B)
  add_edge(G,1,11,A,B)
  add_edge(G,2,9,A,B)
  add_edge(G,2,12,A,B)
  add_matching_edge(G,3,10,A,B)
  add_edge(G,3,11,A,B)
  add_edge(G,3,12,A,B)
  add_edge(G,3,15,A,B)
  add_edge(G,4,10,A,B)
  add_edge(G,4,13,A,B)
  add_matching_edge(G,4,14,A,B)
  add_matching_edge(G,5,12,A,B)
  add_edge(G,5,14,A,B)
  add_edge(G,5,15,A,B)
  add_edge(G,6,12,A,B)
  add_edge(G,6,15,A,B)
  add_edge(G,7,12,A,B)
  add_matching_edge(G,7,15,A,B)
  add_edge(G,8,14,A,B)
  add_edge(G,8,15,A,B)
  add_edge(G,8,16,A,B)
  print(G)
  print(perfect_matching(G,A,B))
  
main()
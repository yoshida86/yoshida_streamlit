import numpy as np
import networkx as nx
from . import prim_heap as heap

def Prim(A):

    MST = [[0 for i in range(len(A))] for i in range(len(A))]

    Vdata = {i: [float('inf'),i,-1] for i in range(len(A))}
    
    N = {i:-1 for i in range(len(A))}
    
    U = heap.Heap()

    s = 0
    Vdata[s][2] = 0
    for j in range(len(A[s])):
        if A[s][j] != 0:
            Vdata[j][0] = A[s][j]
            N[j] = s

            U.insert(Vdata[j])

    while(len(U.data)!=0):

        w = U.deletemin()
        MST[N[w[1]]][w[1]] = A[N[w[1]]][w[1]]
        MST[w[1]][N[w[1]]] = A[w[1]][N[w[1]]]

        for j in range(len(A)):
            if A[w[1]][j] != 0:
                if A[w[1]][j] < Vdata[j][0]:
                    if Vdata[j][2] == -1:
                        Vdata[j][0] = A[w[1]][j]
                        N[j] = w[1]
                        U.insert(Vdata[j])
                    else:
                        Vdata[j][0] = A[w[1]][j]
                        N[j] = w[1]
                        U.update(Vdata[j][2])

    
    return MST,U.opecount

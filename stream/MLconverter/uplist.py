import pandas as pd
import numpy as np

def uplist(file):
    
    df = pd.read_csv(file,header=None)
    df = df.fillna(-1)
    df = df.values.tolist()
    
    mat = []
    for row in range(len(df)):
        tmp = [0 for i in range(len(df))]
        
        for index in df[row][1:]:
            if index != -1:
                tmp[int(index)] = 1
        mat.append(tmp)

    ret = pd.DataFrame(mat)
    return ret


def uplist_weight(file):
    
    df = pd.read_csv(file,header=None)
    df = df.fillna(-1)
    df = df.values.tolist()
    
    mat = []
    for row in range(len(df)):
        tmp = [0 for i in range(len(df))]
        
        for i in range(1,len(df[row]),2):
            if df[row][i] != -1:
                tmp[int(df[row][i])] = df[row][i+1]
        mat.append(tmp)

    ret = pd.DataFrame(mat)
    return ret
import pandas as pd
import numpy as np

def upmat(filepath):

    df = pd.read_csv(filepath,header=None)
    df = df.values.tolist()
    
    todflist = []

    for row in range(len(df)):
        tmp = [row]
        
        for index in range(len(df)):
            if df[row][int(index)] == 1:
                tmp.append(index)
        todflist.append(tmp)

        ret = pd.DataFrame(todflist)
        print(ret)
        
    return ret


def upmat_weight(filepath):

    df = pd.read_csv(filepath,header=None)
    df = df.values.tolist()
    
    todflist = []

    for row in range(len(df)):
        tmp = [row]
        
        for index in range(len(df)):
            if df[row][int(index)] != 0:
                tmp.append(float(index))
                tmp.append(df[row][int(index)])
        todflist.append(tmp)

        ret = pd.DataFrame(todflist,index=None)

        print(ret)
        
    return ret
        


        


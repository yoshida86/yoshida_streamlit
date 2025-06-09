import pandas as pd
from . import prim


def callprim(graph):

    G = graph.values.tolist()

    MST,operation = prim.Prim(G)

    return MST,operation


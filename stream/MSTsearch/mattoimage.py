import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import streamlit as st

def mattond(mat):

    array = np.array(mat)
    return array

    

def MSTimage(G,pos):

    edge_labels = {(i,j): w['weight'] for i,j,w in G.edges(data = True)}

    nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels,font_size=10)
    nx.draw_networkx(G,pos=pos,with_labels = True)

    plt.savefig("MST.png")
    plt.clf()
    return


def graphimage(G,pos):

    edge_labels = {(i,j): w['weight'] for i,j,w in G.edges(data = True)}
    
    nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels,font_size=10)
    nx.draw_networkx(G,pos=pos,with_labels=True)

    plt.savefig("graph.png")
    plt.clf()
    return

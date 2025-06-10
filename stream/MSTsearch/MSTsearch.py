import streamlit as st
import pandas as pd
from . import callprim as callp
from . import mattoimage as mai
import networkx as nx
import numpy as np

def MSTsearch():

    st.title('MSTsearch')

    st.text('隣接行列のcsvを使って、最小全域木の探索ができます')

    graph = st.file_uploader('csvを入力')

    if st.button('実行'):
 
            
        st.divider()
        G = pd.read_csv(graph,header=None,keep_default_na=False)
        
        MST,operation = callp.callprim(G)
        
        G = G.to_numpy()
        MST = np.array(MST)

        graph = nx.Graph(G)
        pos = nx.arf_layout(graph)
        mai.graphimage(graph,pos)
            
        MSTnx = nx.Graph(MST)
        mai.MSTimage(MSTnx,pos)

        before,after= st.columns(2)
            
        with before:
            st.caption('元のグラフ')
            st.image('graph.png')
            
        with after:
            st.caption('最小全域木')
            st.image('MST.png')
            
        st.write(f"ヒープの操作回数: {operation}")
    


    

import streamlit as st
import networkx as nx
import pandas as pd
import numpy as np
from . import upmat as um
from . import uplist as ul

def MLconverter():

    st.title('隣接リスト行列変換機')    

    st.header('※現状、重み付きグラフ非対応')
    st.text('csvで保存された隣接リストと行列を変換、ダウンロードできます。')

    st.divider()
    
    colmat,collist = st.columns(2)
    
    with colmat:

        mat_file = st.file_uploader('隣接行列のcsvの投げ先',type ='csv')

        if mat_file != None:
            if st.button('変換'):
                downloadable_file = um.upmat(mat_file)

                csv = downloadable_file.to_csv(index=None,header=None).encode('utf-8')
                
                st.download_button(label='隣接リストをダウンロード',
                                   data = csv,
                                   file_name = 'processed_list.csv',
                                   mime = 'text/csv')


    with collist:

        list_file = st.file_uploader('隣接リストのcsvの投げ先', type ='csv')

        if list_file != None:
            if st.button('変換'):
                downloadable_file = ul.uplist(list_file)

                csv = downloadable_file.to_csv(index=None,header=None).encode('utf-8')
                
                st.download_button(label='隣接行列をダウンロード',
                                   data = csv,
                                   file_name = 'processed_matrix.csv',
                                   mime = 'text/csv')

import streamlit as st
import networkx as nx
import pandas as pd
import numpy as np
from . import upmat as um
from . import uplist as ul

def MLconverter():

    st.title('隣接リスト行列変換機')    
    st.text('csvで保存された隣接リストと行列を変換、ダウンロードできます。')

    with st.expander('・想定しているcsvの形(重みなしの場合)'):
        lcode,mcode = st.columns(2)

        with lcode:
                
            with open('MLconverter\list.csv') as l:
                code1 = l.read()
            st.caption('隣接リスト')
            st.code(code1)
            st.caption('行の先頭に頂点番号、2要素目から隣接頂点番号')
            
            
        with mcode:
                
            with open('MLconverter\matrix.csv') as m:
                code2 = m.read()
            st.caption('隣接行列')
            st.code(code2)
            st.caption('隣接行列の要素のみ')

    with st.expander('・想定しているcsvの形(重み付きの場合)'):
        lwcode,mwcode = st.columns(2)

        with lwcode:
                
            with open('MLconverter\list_weight.csv') as l:
                code1 = l.read()
            st.caption('隣接リスト')
            st.code(code1)
            st.caption('行の先頭に頂点番号、2要素目からは隣接頂点番号とその辺の重みが交互に')
            
            
        with mwcode:
                
            with open('MLconverter\matrix_weight.csv') as m:
                code2 = m.read()
            st.caption('隣接行列')
            st.code(code2)
            st.caption('隣接行列の要素のみ')

    st.divider()

    weight = st.selectbox('重みの有無を選択してください',['重みなし','重み付き'])
    
    colmat,collist = st.columns(2)
    
    with colmat:

        mat_file = st.file_uploader('隣接行列のcsvの投げ先',type ='csv')

        if mat_file != None and weight == '重みなし':
            if st.button('変換'):

                downloadable_file = um.upmat(mat_file)


                csv = downloadable_file.to_csv(index=None,header=None).encode('utf-8')
                
                st.download_button(label='隣接リストをダウンロード',
                                   data = csv,
                                   file_name = 'processed_list.csv',
                                   mime = 'text/csv')
                
        if mat_file != None and weight == '重み付き':
            if st.button('変換'):

                downloadable_file = um.upmat_weight(mat_file)


                csv = downloadable_file.to_csv(index=None,header=None).encode('utf-8')
                
                st.download_button(label='隣接リストをダウンロード',
                                   data = csv,
                                   file_name = 'processed_list.csv',
                                   mime = 'text/csv')


    with collist:

        list_file = st.file_uploader('隣接リストのcsvの投げ先', type ='csv')

        if list_file != None and weight == '重みなし':
            if st.button('変換'):
                downloadable_file = ul.uplist(list_file)

                csv = downloadable_file.to_csv(index=None,header=None).encode('utf-8')
                
                st.download_button(label='隣接行列をダウンロード',
                                   data = csv,
                                   file_name = 'processed_matrix.csv',
                                   mime = 'text/csv')
                
        if list_file != None and weight == '重み付き':

            if st.button('変換'):
                downloadable_file = ul.uplist_weight(list_file)

                csv = downloadable_file.to_csv(index=None,header=None).encode('utf-8')
                
                st.download_button(label='隣接行列をダウンロード',
                                   data = csv,
                                   file_name = 'processed_matrix.csv',
                                   mime = 'text/csv')



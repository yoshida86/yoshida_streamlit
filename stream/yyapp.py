import streamlit as st
from MSTsearch import MSTsearch as mst
from MLconverter import MLconverter as ml
from home import home

page = st.sidebar.radio('ページ',['home','MSTsearch','MLconverter'])

if page == 'home':

	home.home()
	
if page == 'MSTsearch':
	
	mst.MSTsearch()

if page == 'MLconverter':
	
	ml.MLconverter()

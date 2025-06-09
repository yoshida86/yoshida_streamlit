import streamlit as st

def home():
    
    st.title('ホーム画面')

    st.header('ページ紹介')

    st.subheader('・home')
    st.text('ここ')

    st.subheader('・MSTsearch')
    st.text('最小木探索ができます。')

    st.subheader('・MLconverter')
    st.text('隣接リストを隣接行列に、隣接行列を隣接リストに変換できます\n※入力出力どちらもcsvファイル')

    if st.button('ふうせん'):
        st.balloons()

    
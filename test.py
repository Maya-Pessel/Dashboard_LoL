import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# from plotly.subplots import make_subplots
import plotly.express as px

dataz = pd.read_csv('match_full_time.csv')

# st.title("Titre")

# redwins = dataz[dataz["blue_win"] == 0].shape[0];
# bluewins = dataz[dataz["blue_win"] == 1].shape[0];

# names = ['redwins','bluewins']
# values = ["redwins", "bluewins"]
# df = redwins
# print(df)
# fig = px.pie(redwins, values='blue_win', names='blue_win', hole=.3)

# st.plotly_chart(fig)
st.set_page_config(
     page_title="Dashboard League of Legends",
     page_icon="🌸",
     layout="wide",
     initial_sidebar_state="expanded",
 )

with st.container():
    col1, col2 = st.columns([9, 6])

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col2:

    redwins = dataz[dataz["blue_win"] == 0].shape[0];
    bluewins = dataz[dataz["blue_win"] == 1].shape[0];

    sizes = [redwins, bluewins]
    
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
            shadow=False, startangle=90, colors=['#FE82AF', '#6184FF'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)


with st.container():
    col1, col2 = st.columns([9, 6])

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/owl.jpg")



with st.container():
    col1, col2, col3, col4 = st.columns([6,3,3, 3])

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
    st.header("A pig")
    st.image("https://static.streamlit.io/examples/owl.jpg")





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from plotly.subplots import make_subplots
import plotly.express as px
from matplotlib.patches import Patch




dataz = pd.read_csv('match_full_time.csv')

st.set_page_config(
     page_title="Dashboard League of Legends",
     page_icon="🌸",
     layout="wide",
     initial_sidebar_state="expanded",
 )


with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

 

with st.container():
    col1, col2 = st.columns([7, 5])

with col1:
    st.markdown(""" <style> .font {
    font-size:45px ; padding:50px 0 ; background-color:#ECECEC;   background-color: #ECECEC;
  border-radius: 5px;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dashboard League of Legends</p>', unsafe_allow_html=True)
   
    # st.title('Dashboard League of Legends')


with col2:
     
    legend_elements = [Patch(facecolor='#EABACB',
                            label='Equipe rouge'), Patch(facecolor='#B1BEEB',
                            label='Equipe bleue')]

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#ECECEC')
    ax.set_facecolor("#ECECEC")

    ax.legend(handles=legend_elements, loc='upper center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axis('off')
    plt.subplots_adjust(left=0.5, right=0.8, top=0.6, bottom=0.5)
    st.pyplot(fig)


with st.container():
    col1, col2 = st.columns([5, 7])

with col2:

    labels = ['Bronze', 'Argent', 'Or', 'Platine', 'Diamant',]
    red_means = [48, 46.8, 47.1, 47.7, 47 ]
    blue_means = [52, 53.2, 52.9, 52.3, 53]

    width = 0.35

    fig, ax = plt.subplots(figsize = (10, 5.4))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.bar(labels, red_means, width, label='red', color=[ '#EABACB'])
    ax.bar(labels, blue_means, width, bottom=red_means, label='blue', color=[ '#B1BEEB'])
    plt.axhline(y=50, color='black', linestyle=':')

    ax.set_ylabel('Pourcentages')
    plt.title("Pourcentages de victoires/défaites par rank", fontsize=18)

    fig.patch.set_facecolor('#ECECEC')
    ax.set_facecolor("#ECECEC")
    st.pyplot(fig)


with col1:

    redwins = dataz[dataz["blue_win"] == 0].shape[0];
    bluewins = dataz[dataz["blue_win"] == 1].shape[0];

    sizes = [redwins, bluewins]
    
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, autopct='%1.1f%%',
            shadow=False, startangle=315, colors=['#EABACB', '#B1BEEB'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Pourcentage de victoires globale", fontsize=15)

    fig.patch.set_facecolor('#ECECEC')
    ax.set_facecolor("#ECECEC")
    st.pyplot(fig)



with st.container():
    col1, col2, col3, col4 = st.columns([3,2,2, 2])

with col1:
    st.markdown(""" <style> .text {
     background-color:black; padding :15px; border-radius:5px; background: #ECECEC;
box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.04);} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="text"> En conclusion, on peut observer qu’aussi minime soit elle, qu’une différence subsiste bien entre la moyenne des victoires et de défaite des team rouges et bleu.<br/>La team bleu est toujours légèrement en  tête sur tous les fronts excepté sur le premier dragon abattu.<br/>On peut cependant imaginer pour expliquer ce phénomène par la position de la team rouge. qui est plus favorable pour aller chercher ce premier dragon.<br/><br/>Les données ont été collectées sur 5000 parties en un mois (entre le 07/08/2020 et le 07/09/2020). <br/>Lien du dataset <a href="https://www.kaggle.com/code/kerneler/starter-league-of-legend-lol-result-e3b6e48f-f/data">ici</a>.</p>', unsafe_allow_html=True)

with col2:
    reddrag = dataz[dataz["blue_firstDragon"] == 0].shape[0];
    bluedrag = dataz[dataz["blue_firstDragon"] == 1].shape[0];
    data = {'Rouge':reddrag, 'Bleue':bluedrag}

    Courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize = (5, 7.3))
    ax = fig.add_axes([0, 0, 1, 1])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    fig.patch.set_facecolor('#ECECEC')
    ax.set_facecolor("#ECECEC")
    plt.bar(Courses, values, color=['#EABACB', '#B1BEEB'])
    plt.ylabel("Nombre de parties", fontsize=20)    
    plt.title("Premier dragon de la partie", fontsize=30)

    st.pyplot(fig)
    
with col3:
    redfb = dataz[dataz["blue_firstBlood"] == False].shape[0];
    bluefb = dataz[dataz["blue_firstBlood"] == True].shape[0];
    data = {'Rouge':redfb, 'Bleue':bluefb}

    Courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize = (5, 7))
    ax = fig.add_axes([0, 0, 1, 1])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    fig.patch.set_facecolor('#ECECEC')
    ax.set_facecolor("#ECECEC")

    plt.bar(Courses, values, color=['#EABACB', '#B1BEEB'])
    plt.ylabel("Nombre de parties", fontsize=20)    
    plt.title("Premier sang de la partie", fontsize=30)

    st.pyplot(fig)

with col4:
    redtower = dataz[dataz["blue_firstTower"] == False].shape[0];
    bluetower = dataz[dataz["blue_firstTower"] == True].shape[0];
    data = {'Rouge':redtower, 'Bleue':bluetower}

    Courses = list(data.keys())
    values = list(data.values())


    fig = plt.figure(figsize = (5, 7))
    ax = fig.add_axes([0, 0, 1, 1])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    fig.patch.set_facecolor('#ECECEC')
    ax.set_facecolor("#ECECEC")

    plt.bar(Courses, values, color=['#EABACB', '#B1BEEB'])
    plt.ylabel("Nombre de parties", fontsize=20)    
    plt.title("Premiere tour de la partie", fontsize=30)

    st.pyplot(fig)





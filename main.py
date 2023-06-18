# -*- coding: utf-8 -*-
"""
Created on Sat June  17 

@author: Salim Dallal
""" 


#import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st
import pandas as pd
# import numpy as np
# import plotly.graph_objects as gos
import altair as alt
from PIL import Image
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# from sklearn.preprocessing import StandardScaler



st.set_page_config(
    page_title="Economic crisis Impact on Lebanon's Burden of Desease",
    page_icon=":bar_chart:",
    layout="wide"
)



###################################################################################################################################################################
# Creating the Side Bar Navigation Panel

imgside=Image.open('./Sidebar.jpg')
st.sidebar.image(imgside, use_column_width=True)

navigate = st.sidebar.radio('Navigation Side Bar',
                 ('Home Page', 'Location based Dashboard', 'Gender based Dashboard', 'Recommendations'))


# Updating the Datset if needed
# uploaded_file = st.file_uploader("Upload updated dataset")
# if uploaded_file is None:
df = pd.read_csv("./Data.csv")
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
if st.button('Show a sample of the data'):
    st.write(df.head())
#####################################################################################################################################################################
# df.head()        
# df.describe()

#checking for null values
# df.isna().sum()

#features info
# df.info()


# Creating the Home Page

if navigate == 'Home Page':
    # adding title
    title_col = st.columns(1)
    title_col[0].title("Economic crisis Impact on Lebanon's Burden of Desease")
    
    
    # adding the home page image
    img=Image.open('./image.jpg')
    st.image(img)

    
    # dashboard description
    st.header("Context")
    st.markdown("""Heart failure is a common event caused by cardiovascular diseases. Cardiovascular diseases (CVDs) are the number one cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of Five CVD deaths are due to heart failures, and one-third of these deaths occur prematurely in people under 70 years of age. 
    People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidemia or already established disease) need early detection and management wherein a machine learning model can be of great help.
    """)
    # dataset info
    st.header("Dataset Information")
    st.markdown("""The dataset contains 11 features that can be used to predict a possible heart disease. It includes 12 variables describing 918 observations.
                Data is collected and combined from Five heart datasets with 11 common features which makes this dataset large and reach enough for research and educational purposes.""")

    
# Creating the Dashboard Page

if navigate == 'Location based Dashboard':
    st.title(":bar_chart: Statistics")
    st.markdown("##")
    
    Measure = st.sidebar.selectbox(
        "Select the Measure",
        options=df["measure"].unique(),
        index=1
        )

    Metric = st.sidebar.selectbox(
        "Select the Metric",
        options=df["metric"].unique(),
        index=0
        )
        
    
    Location = st.sidebar.multiselect(
        "Select the Location(s):",
        options=df["location"].unique(),
        default="Lebanon" #df["location"].unique()
        )


    Gender = st.sidebar.multiselect(
         "Select the Gender:",
         options=df["sex"].unique(),
         default="Both"
         )


    # adding an aligned title without using CSS
    st.markdown("<h1 style='text-align: center; color: blue;'>Exploratory Analysis of the Global Burden of Disease trends</h1>", unsafe_allow_html=True)
  
    #st.dataframe(df_selection[["measure","location","sex","age","cause","rei","metric","year","val","upper","lower"]])

    for x in Gender:
        
        df_selection = df.query(
            "location == @Location & sex == @x & measure == @Measure & metric == @Metric & age == 'All ages'"
            )
        
        chart = alt.Chart(df_selection).mark_line().encode(
              x=alt.X('year:N'),
              y=alt.Y('val:Q'),
              color=alt.Color("location:N")
            ).properties(title="Compare GBD by Locaion for " + x)
        st.altair_chart(chart, use_container_width=True)
        


# Creating the Dashboard Page
if navigate == 'Gender based Dashboard':
    st.title(":bar_chart: Statistics")
    st.markdown("##")
    
    Measure = st.sidebar.selectbox(
        "Select the Measure",
        options=df["measure"].unique(),
        index=1
        )

    Metric = st.sidebar.selectbox(
        "Select the Metric",
        options=df["metric"].unique(),
        index=1
        )
    
    
    Gender = st.sidebar.multiselect(
        "Select the Gender:",
        options=df["sex"].unique(),
        default=["Male","Female"]
        )
    
    AgeGroup = st.sidebar.multiselect(
        "Select the age group:",
        options=df["age"].unique(),
        default="All ages"
        )

    # adding an aligned title without using CSS
    st.markdown("<h1 style='text-align: center; color: blue;'>Exploratory Analysis of the Global Burden of Disease trends</h1>", unsafe_allow_html=True)
    
    #st.dataframe(df_selection[["measure","location","sex","age","cause","rei","metric","year","val","upper","lower"]])
    

    for x in AgeGroup:
        
        df_selection = df.query(
            "sex == @Gender & measure == @Measure & metric == @Metric & age == @x"
            )
        
        chart = alt.Chart(df_selection).mark_bar().encode(
              x=alt.X('year:N'),
              y=alt.Y('val:Q'),
              color=alt.Color("sex:N")
            ).properties(title="Compare GBD by Sex for ages " + x)
        st.altair_chart(chart, use_container_width=True)
        
########################################################################################################################################################################


if navigate == 'Recommendations':
    # adding title
    title_col = st.columns(1)
    title_col[0].title("Recommendation")
    
    
    
    # dashboard description
    st.header("Context")
    st.markdown("""Heart failure is a common event caused by cardiovascular diseases. Cardiovascular diseases (CVDs) are the number one cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of Five CVD deaths are due to heart failures, and one-third of these deaths occur prematurely in people under 70 years of age. 
    People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidemia or already established disease) need early detection and management wherein a machine learning model can be of great help.
    """)
    # dataset info
    st.header("Dataset Information")
    st.markdown("""The dataset contains 11 features that can be used to predict a possible heart disease. It includes 12 variables describing 918 observations.
                Data is collected and combined from Five heart datasets with 11 common features which makes this dataset large and reach enough for research and educational purposes.""")

    
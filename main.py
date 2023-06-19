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
                 ('Home Page', 'Location based Dashboard', 'Age based Dashboard', 'Recommendations'))


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
    st.markdown("""The Global Burden of Disease is a comprehensive assessment of health conditions, risk factors, and causes of death across various populations and regions. By analyzing GBD data, we can gain insights into the prevailing health issues, disease prevalence, and the burden experienced by a specific population. In the case of Lebanon, understanding the GBD trends is crucial for recognizing the demand for healthcare services and planning for future needs especially with the new circumstances affecting the country. In recent years, Lebanon has succumbed to an economic crisis believed to the worst in recent history. This crisis to bound to affect all aspects of life and to have an enormous effect on the healthcare system. This is evident in the numerous articles and numbers indicating many problems stressing out the health care system. 
    """)
    
    st.markdown("""Two major issues are the exodus of heath care practitioners and the decrease in the availability of attainable medications. It is estimated that by January 2022 40 percent of health care professionals have left the country in search of better offers abroad. Many of these were specialized professionals serving specific diseases such as cancer, heart disease, and pediatrics just to name a few. Many of the private hospitals where these professionals worked had to shut down their departments. 
    """)
    
    st.markdown("""As for medications, different difficulties have arisen. starting from the availability of these medications all the way to their extreme high prices and removal of subsidization. Due to the crisis and the lack of trust in banks and the inflexibility of laws regarding medication financing, medication suppliers are not able to import the needed medications even if the funds are available. Many of the medications are required to be subsidized by the government and cannot be imported otherwise. With the government going bankrupt, subsidization was at a halt and the critical mediation like Cancer medications were not available anymore. Eventually the Ministry of Public Health slowly started to allow import of such supplies without subsidization, however, this made them available only to the wealthy population since they are now extremely expensive
    """)
    
    
    # dataset info
    st.header("Dataset Information")
    st.markdown("""We have used data from the Global Burden of Disease section of the Institute for Health Metrics and Evaluation (IHME) website. The Data in its nature is mainly quantitative primary data. 

Four measures are used:
1.	Deaths
2.	DALYs (Disability Adjusted Life Years)
3.	YLDs (Years Lived with Disability) 
4.	YLLs (Years of Life Lost)	

Three Metrics:
1.	Number
2.	Percent
3.	Rate (per 100,000 population)

Locations used for comparison:
1.	Lebanon
2.	World Bank Low Income
3.	World Bank Lower Middle Income
4.	World Bank Upper Middle Income
5.	World Bank High Income	

Other Data available to use:
Age groups: 0-14, 15-19, 20-54, and 55+
Gender: Male, Female, and both
Years: 2000 - 2019

Data retrieved from the IHME website is already cleaned. It doesn’t have any empty or null values, and is mostly aggregated.
We are using python with Streamlit, Pandas, and Altair packages to draw the graphs and charts. The aim is to compare the GBD of Lebanon with the GBD of the different income bounds as differentiated by the World bank. The main idea is to see what the effect in case Lebanon moves from one Location to another due to its economic crisis. We will see if there are differences among age groups and the sexes.

Limitations to this approach are:
•	Lebanon’s case is the first of its kind, as such factors governing the reporting of data, collection of data, and it’s accuracy may be the same as the location Lebanon belonged to pre-2019 crisis but may differ 
•	Data gathered is up to the year 2019. It doesn’t cover the timespan of the crisis.
•	There may be other indices that may be prevalent and need to be studied which are not included in this dataset.
                """)

    
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
        index=2
        )
        
    
    Location = st.sidebar.multiselect(
        "Select the Location(s):",
        options=df["location"].unique(),
        default="Lebanon" #df["location"].unique()
        )


    Sex = st.sidebar.multiselect(
         "Select the Sex:",
         options=df["sex"].unique(),
         default="Both"
         )


    # adding an aligned title without using CSS
    st.markdown("<h1 style='text-align: center; color: blue;'>Exploratory Analysis of the Global Burden of Disease trends</h1>", unsafe_allow_html=True)
  
    #st.dataframe(df_selection[["measure","location","sex","age","cause","rei","metric","year","val","upper","lower"]])

    for x in Sex:
        
        df_selection = df.query(
            "location == @Location & sex == @x & measure == @Measure & metric == @Metric & age == 'All ages'"
            )
        
        chart = alt.Chart(df_selection).mark_line().encode(
              x=alt.X('year:N'),
              y=alt.Y('val:Q'),
              color=alt.Color("location:N")
            ).properties(title="Compare GBD " + Metric + " by Location for " + x)
        st.altair_chart(chart, use_container_width=True)
        


# Creating the Dashboard Page
if navigate == 'Age based Dashboard':
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
        index=2
        )
    
    
    Sex = st.sidebar.multiselect(
        "Select the Sex:",
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
            "sex == @Sex & measure == @Measure & metric == @Metric & age == @x"
            )
        
        chart = alt.Chart(df_selection).mark_bar().encode(
              x=alt.X('year:N'),
              y=alt.Y('val:Q'),
              color=alt.Color("sex:N")
            ).properties(title="Compare GBD " + Metric + " by Sex for ages " + x)
        st.altair_chart(chart, use_container_width=True)
        
########################################################################################################################################################################


if navigate == 'Recommendations':
    # adding title
    title_col = st.columns(1)
    title_col[0].title("Recommendation")
    
    
    
    # dashboard description
    # st.header("Context")
    st.markdown("""Form the dashboards above, if Lebanon moves to a lower income country category, the burden of disease will increase. It is highly recommended to increase the level of income to alleviate such risks. Other methods of alleviation may be present by changing the Healthcare system model to a Universal Model that is funded by the government or via External Grants in contrast to the current existing model where 80% of health institutions are Private and most people in Lebanon cannot afford them anymore.
                """)
    # dataset info
    st.markdown("""It is worth noting that the available data does not however provide a direct causality or even show similar situations since Lebanon’s crisis is not precedented at this scale. The data at hand does not present enough information on which age groups may be affected most with this crisis. It is recommended to acquire data post the year 2019 to better understand the impact of the ongoing economic crisis along with the Covid 19 pandemic and the port blast disaster.""")

    
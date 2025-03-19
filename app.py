import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import Image


# Custom CSS for styling the title

st.markdown(
    """
    <style>
    .title {
        color: CornflowerBlue;
        font-size: 26px;
        text-align: left;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        text-shadow: 1px 1px24px #000000;
        border-bottom: 3px solid #add8e6;
        padding-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Model metrics

col3, col4, col5 = st.columns(3)

col3.metric("Model Accuracy", "90%")
col4.metric("Model Precision", "90%")
col5.metric("Model Recall", "87%")


# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;  /* Light blue background */
    }
    h1 {
        color: darkblue;
        text-align: center;
    }
    .stMetric {
        font-size: 24px;  /* Custom font size for metrics */
    }
    .stImage {
        border-radius: 10px;  /* Rounded corners for the image */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("########################## :")

comfort = st.number_input("Comfort (%)", min_value=0, max_value=100, step = 10)/100

culture = st.number_input("Culture (%)",min_value=0, max_value=100, step = 10)/100

crowding = st.number_input("Crowding (%)",min_value=0, max_value=100, step = 10)/100

cost_living = st.number_input("Cost of Living (%)",min_value=0, max_value=100, step = 10)/100

security = st.number_input("Security (%)",min_value=0, max_value=100, step = 10)/100

connectivity  = st.number_input("Connectivity (%)",min_value=0, max_value=100, step = 10)/100

reliability = st.number_input("Reliability (%)",min_value=0, max_value=100, step = 10)/100


# Button for prediction
st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("Predict"):

    if comfort + culture + crowding + cost_living + security + connectivity + reliability == 1:

        st.balloons()

        df=pd.read_csv("raw_data/ranking_w.csv")

        df.drop(columns = "Final_Score", inplace = True)

        df["Final_Score"] = df.Culture*culture + df.Comfort*comfort + df.Crowding*crowding + df.Cost_of_Living*cost_living + df.Security*security + df.Connectivity*connectivity + df.Reliability*reliability

        df_final = df[["Line", "Final_Score"]].sort_values(by = "Final_Score", ascending = False).reset_index(drop = True)

        favorite_line = df_final["Line"][0]


        st.write(f"Your favorite line is the {favorite_line} line")

        st.markdown(f"""
        WELCOME TO THE {favorite_line} LINE
        """)

        from PIL import Image

        # image = Image.open(f'raw_data/{favorite_line}.png'))
        # st.image(image, use_column_width=False)
        st.write("And this is the ranking of the lines based on your preferences:")

        st.write(df_final)

        st.balloons()


    else:

        st.write("The sum of the values should be 100")
    st.markdown('</div>', unsafe_allow_html=True)

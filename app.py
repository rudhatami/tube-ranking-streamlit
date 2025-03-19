import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



# Custom CSS for styling the title

st.markdown(
    """
    <style>
    .title {
        color: SafetyBlue;
        font-size: 50px;
        text-align: left;
        font-family: 'Gill Sans';
        font-weight: bold;
        text-shadow: 1px 1px24px #000000;
        border-bottom: 3px solid #add8e6;
        padding-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)



#import cairosvg
#cairosvg.svg2png(url="raw_data/tfl_logo.svg", write_to="raw_data/tfl_logo.png")

#from PIL import Image
#import streamlit as st

img = Image.open("raw_data/tfl_logo.svg.png")
st.image(img)





# st.raw_data/tfl_logo.svg.png
# Model metrics

col3, col4, col5 = st.columns(3)

# col3.metric("Model Accuracy", "90%")
# col4.metric("Model Precision", "90%")
# col5.metric("Model Recall", "87%")


# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #0025A8;  /* Light blue background */
    }
    h1 {
        color: #E1251B;
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

st.markdown("<h3 class = 'title'> Welcome to your individualised Ranking : </h3>", unsafe_allow_html = True)


# Create three columns
col1, col2, col3, col4 = st.columns(4)

# Distribute input fields across columns
with col1:
     security = st.number_input("Security (%)", min_value=0, max_value=100, step=10) / 100
     comfort = st.number_input("Comfort (%)", min_value=0, max_value=100, step=10) / 100
    
with col2:
     crowding = st.number_input("Crowding (%)", min_value=0, max_value=100, step=10) / 100
     culture = st.number_input("Culture (%)", min_value=0, max_value=100, step=10) / 100
with col3:
    reliability = st.number_input("Reliability (%)", min_value=0, max_value=100, step=10) / 100
    cost_living = st.number_input("Cost of Living (%)", min_value=0, max_value=100, step=10) / 100
with col4:
    connectivity = st.number_input("Connectivity (%)", min_value=0, max_value=100, step=10) / 100


# col1, col2, col3 = st.columns(3)

# comfort = st.number_input("Comfort (%)", min_value=0, max_value=100, step = 10)/100

# culture = st.number_input("Culture (%)",min_value=0, max_value=100, step = 10)/100

# crowding = st.number_input("Crowding (%)",min_value=0, max_value=100, step = 10)/100

# cost_living = st.number_input("Cost of Living (%)",min_value=0, max_value=100, step = 10)/100

# security = st.number_input("Security (%)",min_value=0, max_value=100, step = 10)/100

# connectivity  = st.number_input("Connectivity (%)",min_value=0, max_value=100, step = 10)/100

# reliability = st.number_input("Reliability (%)",min_value=0, max_value=100, step = 10)/100


# Button for prediction
st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("Predict"):

    if comfort + culture + crowding + cost_living + security + connectivity + reliability == 1:

        st.balloons()

        df=pd.read_csv("raw_data/ranking.csv")

        df.drop(columns = "Overall_Score", inplace = True)

        df["Final_Score"] = df.Culture*culture + df.Comfort*comfort + df.Crowding_update*crowding + df.Cost_of_Living_update*cost_living + df.Security_update*security + df.Connectivity*connectivity + df.Reliability*reliability

        df_final = df[["line", "Final_Score"]].sort_values(by = "Final_Score", ascending = False).reset_index(drop = True)

        favorite_line = df_final["line"][0]


        # st.write(f"It's official! Your favorite line is the {favorite_line} line")

        st.markdown(f"**Your favorite line is officially the {favorite_line} line!**")

        # st.markdown(f"""
        # WELCOME TO THE {favorite_line} LINE
        # """)

        st.image(f"raw_data/{favorite_line}.png")
        
        st.write("And this is your personalised tube line ranking based on your preferences:")
        
        df_final.index = df_final.index + 1
        st.write(df_final)

        st.balloons()


    else:

        st.write("The sum of the values should be 100")
    st.markdown('</div>', unsafe_allow_html=True)

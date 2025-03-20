import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# Inject custom CSS to change the font to Hammersmith One
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Hammersmith+One&display=swap');
        
        /* Apply the font globally */
        * {
            font-family: 'Hammersmith One', sans-serif;
        }
        
        /* Specific font settings for headers, including the title */
        h1, h2, h3, h4, h5, h6, .css-1d391kg {
            font-family: 'Hammersmith One', sans-serif;
        }
        
        /* For the main title (st.title) */
        .css-1y4kczv {
            font-family: 'Hammersmith One', sans-serif;
        }
        /* Styling for the button */
        .css-1emrehy {
            font-family: 'Hammersmith One', sans-serif;
            background-color: #4B56FF;  /* New background color */
            color: white;  /* Text color */
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 20px;
            font-weight: bold;
            border: none;
        }

        /* Center the button with a custom div class */
        .center-button {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
    </style>
    """, unsafe_allow_html=True)




# Custom CSS for styling the title

st.markdown(
    """
    <style>
    .title {
        color: #0009AB;
        font-size: 100px;
        text-align: left;
        font-family: 'Hammersmith One';
        font-weight: bold;
        text-shadow: 1px 1px24px #000000;
        border-bottom: 3px solid ##0009AB;
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

# col3, col4, col5 = st.columns(3)

# col3.metric("Model Accuracy", "90%")
# col4.metric("Model Precision", "90%")
# col5.metric("Model Recall", "87%")


# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #DE2110  /* Light blue background */
    }
    h1 {
        color: #DE2110;
        text-align: center;
    }
    .stMetric {
        font-size: 40px;  /* Custom font size for metrics */
    }
    .stImage {
        border-radius: 10px;  /* Rounded corners for the image */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <h2 style="font-weight: bold; color: #4B56FF;">
    <br><br>
        Welcome to your individualised <strong>Ranking</strong>! 
    </h2>
    <br><br>
    <h4 style="font-size: 18px; font-weight: normal;">
        Please weigh the below <strong>factors</strong> in terms of your priorities when taking the <strong>tube</strong>:
    </h4>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        .custom-label {
            font-size: 25px !important;
            font-weight: bold;
            color: #4B56FF; /* Change text color if needed */
        }
    </style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)


with col1:
     security = st.number_input("Security (%)", min_value=0, max_value=100, step=10) / 100
    
with col2:
     crowding = st.number_input("Crowding (%)", min_value=0, max_value=100, step=10) / 100
    
with col3:
    reliability = st.number_input("Reliability (%)", min_value=0, max_value=100, step=10) / 100



col4,col5, col6, col7 = st.columns(4)
with col4:
    connectivity = st.number_input("Connectivity (%)", min_value=0, max_value=100, step=10) / 100
with col5:
     comfort = st.number_input("Comfort (%)", min_value=0, max_value=100, step=10) / 100
    
with col6:
     culture = st.number_input("Culture (%)", min_value=0, max_value=100, step=10) / 100
with col7:
    cost_living = st.number_input("Cost of Living (%)", min_value=0, max_value=100, step=10) / 100





# col1, col2, col3 = st.columns(3)

# comfort = st.number_input("Comfort (%)", min_value=0, max_value=100, step = 10)/100

# culture = st.number_input("Culture (%)",min_value=0, max_value=100, step = 10)/100

# crowding = st.number_input("Crowding (%)",min_value=0, max_value=100, step = 10)/100

# cost_living = st.number_input("Cost of Living (%)",min_value=0, max_value=100, step = 10)/100

# security = st.number_input("Security (%)",min_value=0, max_value=100, step = 10)/100

# connectivity  = st.number_input("Connectivity (%)",min_value=0, max_value=100, step = 10)/100

# reliability = st.number_input("Reliability (%)",min_value=0, max_value=100, step = 10)/100

total = int(round((comfort + culture + crowding + cost_living + security + connectivity + reliability) * 100))
st.write(f'The sum of your total should be 100/ {total}')


# Button for prediction
st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("Predict"):

    if comfort + culture + crowding + cost_living + security + connectivity + reliability == 1:

        st.balloons()

        df=pd.read_csv("raw_data/ranking.csv")

        df.drop(columns = "Overall_Score", inplace = True)

        df["Score"] = df.Culture*culture + df.Comfort*comfort + df.Crowding_update*crowding + df.Cost_of_Living_update*cost_living + df.Security_update*security + df.Connectivity*connectivity + df.Reliability*reliability

        df_final = df[["line", "Score"]].sort_values(by = "Score", ascending = False).reset_index(drop = True)
        
        df_final.rename(columns={"line": "Line"}, inplace=True)
        df_final["Rank"] = df_final.index +1 
        df_final = df_final[["Rank", "Line", "Score"]]
        df_final.set_index("Rank", inplace=True)
        favorite_line = df_final["Line"].iloc[0]
       
        
        # df_final.drop(columns = "line", inplace = True)
        # df_final['Rank'] = df_final.index + 1
        # df_final = df_final[["Rank", "Line", "Score"]]
        # st.write(df_final.style.hide(axis="index"))
         # favorite_line = df_final["Line"][0]
        


        # st.write(f"It's official! Your favorite line is the {favorite_line} line")

        
#         st.markdown("""
#         <br><br>
#         <p style="
#         text-align: center; 
#         font-size: 50px; 
#         font-weight: bold; 
#         background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); 
#         -webkit-background-clip: text; 
#         color: transparent;">
#         It's official!!
#         </p>
#         <br><br>
#         <h2 style="text-align: center;">
#         </h2>
#         <br><br><br><br>
#         """, unsafe_allow_html=True)
#         st.markdown(f"""
#     <p style="font-size: 20px; font-weight: normal; text-align: left;">
#         Your favorite line is the {favorite_line} line!
#     </p>
#     <br><br><br><br>
# """, unsafe_allow_html=True)

        st.markdown("""
    <p style="
        text-align: center; 
        font-size: 50px; 
        font-weight: bold; 
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); 
        -webkit-background-clip: text; 
        color: transparent;
        margin-bottom: 10px;">
        It's official!!
        </p>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <p style="font-size: 24px; font-weight: bold; text-align: center; margin-top: 5px;">
        Your favorite line is the {favorite_line} line!
        </p>
        """, unsafe_allow_html=True)




        # st.markdown(f"""
        # WELCOME TO THE {favorite_line} LINE
        # """)

        st.image(f"raw_data/{favorite_line}.png")
        
        

        st.markdown(f"""
        <p style="font-size: 22px; font-weight: normal; text-align: left; margin-top: 5px;">
        <br><br><br><br>And this is the ranking based on your personal preference:
        </p>
        """, unsafe_allow_html=True)

        
        # st.write(df_final)
        
# Custom CSS for dataframe styling
        st.markdown("""
            <style>
            .streamlit-expanderHeader {
                font-weight: bold;
            }
            
            .dataframe-container {
                border: 2px solid blue;
                padding: 10px;
                border-radius: 10px;
            }
        
            .dataframe-container th {
                font-size: 22px;
                font-weight: bold;
                color: black;
            }
        
            .dataframe-container td {
                font-size: 25px;
            }
        
            .dataframe-container td, .dataframe-container th {
                padding: 10px;
                text-align: center;
            }
        
            /* Making columns smaller */
            .dataframe-container table {
                width: 40%;
            }
            </style>
        """, unsafe_allow_html=True)
        
        # Display the dataframe
        st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
        st.dataframe(df_final, width=300)
        st.markdown('</div>', unsafe_allow_html=True)
    #     st.markdown("""
    #     <style>
    #     .styled-table {
    #         border: 2px solid blue;
    #         padding: 10px;
    #         border-radius: 10px;
    #         width: 60%;  /* Control the width of the table */
    #         margin: auto;
    #     }
    
    #     .styled-table th {
    #         font-size: 22px;
    #         font-weight: bold;
    #         color: black;
    #         text-align: center;
    #     }
    
    #     .styled-table td {
    #         font-size: 18px;
    #         text-align: center;
    #     }
    
    #     .styled-table td, .styled-table th {
    #         padding: 10px;
    #     }
    
    #     .styled-table th, .styled-table td {
    #         width: 20%;
    #     }
    #     </style>
    # """, unsafe_allow_html=True)
    
    # # Display the dataframe using st.write() with a custom class
    #     st.markdown('<table class="styled-table">', unsafe_allow_html=True)
    #     st.write(df_final)
    #     st.markdown('</table>', unsafe_allow_html=True)

# Store the top-ranked line
        

        st.balloons()


else:

        st.write("The sum of the values should be 100")
        st.markdown('</div>', unsafe_allow_html=True)


# with col1:
#      security = st.number_input("Security (%)", min_value=0, max_value=100, step=10) / 100
#      comfort = st.number_input("Comfort (%)", min_value=0, max_value=100, step=10) / 100
    
# with col2:
#      crowding = st.number_input("Crowding (%)", min_value=0, max_value=100, step=10) / 100
#      culture = st.number_input("Culture (%)", min_value=0, max_value=100, step=10) / 100
# with col3:
#     reliability = st.number_input("Reliability (%)", min_value=0, max_value=100, step=10) / 100
#     cost_living = st.number_input("Cost of Living (%)", min_value=0, max_value=100, step=10) / 100
# with col4:
#     connectivity = st.number_input("Connectivity (%)", min_value=0, max_value=100, step=10) / 100
    
#     total = comfort + culture + crowding + cost_living + security + connectivity + reliability
#     st.write(f'This is the sum of your total: {total}')


# col5, col6, col7 = st.columns(3)

# with col5:
#      comfort = st.number_input("Comfort (%)", min_value=0, max_value=100, step=10) / 100
    
# with col6:
#      culture = st.number_input("Culture (%)", min_value=0, max_value=100, step=10) / 100
# with col7:
#     cost_living = st.number_input("Cost of Living (%)", min_value=0, max_value=100, step=10) / 100

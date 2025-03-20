import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import seaborn as sns  # Import seaborn at the top of your script


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
    <h5 style="font-size: 10px; font-weight: normal;">
        *Scroll down for a breakdown of the metrics.
    </h5>
""", unsafe_allow_html=True)

st.markdown("""
    <h5 style="font-size: 10px; font-weight: normal;">
        *Scroll down for a breakdown of the metrics.
    </h5>
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
st.write(f'Sum of your total: {total}/100')


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
        <p style="font-size: 16px; font-weight: normal; text-align: left; margin-top: 5px;">
        <br><br><br><br>And this is the ranking based on your personal preference:
        </p>
        """, unsafe_allow_html=True)

        
        # st.write(df_final)
        
# Custom CSS for dataframe styling
        # st.markdown("""
        #     <style>
        #     .streamlit-expanderHeader {
        #         font-weight: bold;
        #     }
        #     # .dataframe-container {
        #     # display: flex;
        #     # justify-content: center;
        #     # align-items: center;
        #     # height: 100vh;  /* Full screen height to center the content vertically */
        #     # width: 100%;
        #     # }
        #     # .dataframe-container {
        #     #     border: 2px solid blue;
        #     #     padding: 10px;
        #     #     border-radius: 10px;
        #     # }
        
        #     .dataframe-container th {
        #         font-size: 30px;
        #         font-weight: bold;
        #         color: black;
        #     }
        
        #     .dataframe-container td {
        #         font-size: 30px;
        #     }
        
        #     .dataframe-container td, .dataframe-container th {
        #         padding: 10px;
        #         text-align: center;
        #     }
        
        #     /* Making columns smaller */
        #     .dataframe-container table {
        #         width: 40%;
        #     }
        #     </style>
        # """, unsafe_allow_html=True)
        
        # # Display the dataframe
        # st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
        # st.dataframe(df_final, width=300)
        # st.markdown('</div>', unsafe_allow_html=True)
        # st.markdown("""
        #     <style>
        #     /* Center the dataframe container on the page */
        #     .dataframe-container {
        #         display: flex;
        #         justify-content: center;
        #         align-items: center;
        #         height: 100vh;  /* Center vertically */
        #         width: 100%;
        #         padding: 20px;
        #         box-sizing: border-box;
        #     }
        
        #     /* Styling for the table */
        #     .dataframe-container table {
        #         width: 50%;  /* Make the table narrower */
        #         border-collapse: collapse;  /* Merge borders to make it clean */
        #     }
        
        #     /* Column header styling */
        #     .dataframe-container th {
        #         font-size: 24px;  /* Larger font size */
        #         font-weight: bold;  /* Bold column names */
        #         color: black;
        #         border: 2px solid #4B56FF;  /* Border color for header */
        #         padding: 12px;  /* Add padding for clarity */
        #         text-align: center;
        #     }
        
        #     /* Cell styling */
        #     .dataframe-container td {
        #         font-size: 20px;  /* Larger font size for the values */
        #         border: 2px solid #4B56FF;  /* Border color for cell */
        #         padding: 12px;
        #         text-align: center;
        #     }
        
        #     /* Centering the dataframe */
        #     .css-ffhzg2 { 
        #         display: flex;
        #         justify-content: center;
        #     }
        
        #     </style>
        # """, unsafe_allow_html=True)
        
        # # Wrap the dataframe with a custom container for styling
        # st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
        
        # # Display the dataframe in the styled container
        # st.dataframe(df_final, use_container_width=False)
        
        # # Close the container div
        # st.markdown('</div>', unsafe_allow_html=True)

        

        # col1, col2, col3 = st.columns(spec = [1, 2, 1])

        # with col2:
        #      cm = sns.color_palette("coolwarm_r", as_cmap=True)  # Generate the color map
        #      df_final = df_final.style.background_gradient(cmap=cm)  # Apply the gradient style
        #      st.dataframe(df_final)  # Display the styled dataframe
# Example DataFrame (replace with your own df_final)



# # Example DataFrame (replace with your own df_final)
#         df_final = pd.DataFrame({
#             'Line': df_final["line"],
#             'Score': df_final["Score"]
#         })
        
#         # Style the dataframe
#         df_final = df_final.style.set_table_styles(
#             [
#                 {'selector': 'th', 
#                  'props': [('font-size', '20px'), ('font-weight', 'bold'), ('text-align', 'center')]},  # Column names
#                 {'selector': 'td', 
#                  'props': [('font-size', '18px'), ('text-align', 'center')]},  # Data rows
#                 {'selector': 'thead th', 
#                  'props': [('background-color', '#D3D3D3')]},  # Highlight first row (headers) color
#                 {'selector': 'tbody tr:nth-child(1)', 
#                  'props': [('background-color', '#FFEB3B')]}  # Highlight the first row in yellow
#             ]
#         ).hide(axis="index")  # Hide the index column
        
#         # Display the styled dataframe
        col1, col2, col3 = st.columns([1, 2, 1])  # Columns to center it
        with col2:
            st.write(df_final)




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
        st.markdown("""
        <p style="color: red; font-size: 20px;">
        The sum of the values should be 100
        </p>
        """, unsafe_allow_html=True)

        # st.write("The sum of the values should be 100")
        # st.markdown('</div>', unsafe_allow_html=True)

# st.markdown("""
#     Explanation to the metrics:<br><br>
#     **Security**: This metric evaluates the safety of each line, considering the frequency of accidents and crimes across different boroughs.<br><br>
#     **Crowding**: This metric gauges how busy each line is, assessing passenger density during peak hours. <br><br>
#     **Reliability**: Measures the dependability of each line, based on factors like delays, lost customer hours, journey access time, percentage of services operated, and the proportion of kilometers covered.<br><br>
#     **Connectivity**: Evaluates how well each line connects with other transport options, including transfers to underground lines, other public transport, the Night Tube, access lengths, average speeds, and the number of boroughs served.<br><br>
#     **Comfort**: Assesses the overall comfort level of a line, including noise levels, air quality, temperature, depth of the line (underground), internet connection, and cleanliness.<br><br>
#     **Cost of Living**: This metric reflects the affordability of the boroughs served by each line, based on average rent, housing prices, and the cost of living, including pint prices.<br><br>
#     **Culture**: Measures the cultural richness of the boroughs served by each line, based on the number of cultural sites, box office revenues, and the number of movies filmed in those areas.<br><br><br><br>

# """, unsafe_allow_html=True)
# st.markdown("""
#     <p style="font-size: 18px; font-weight: bold;">
#     Explanation of the metrics:
#     </p>
#     <p style="font-size: 14px;">
#     <u><strong>Security</strong></u>: This metric evaluates the safety of each line, considering the frequency of accidents and crimes across different boroughs.<br><br>
#     <u><strong>Crowding</strong></u>: This metric gauges how busy each line is, assessing passenger density during peak hours. <br><br>
#     <u><strong>Reliability</strong></u>: Measures the dependability of each line, based on factors like delays, lost customer hours, journey access time, percentage of services operated, and the proportion of kilometers covered.<br><br>
#     <u><strong>Connectivity</strong></u>: Evaluates how well each line connects with other transport options, including transfers to underground lines, other public transport, the Night Tube, access lengths, average speeds, and the number of boroughs served.<br><br>
#     <u><strong>Comfort</strong></u>: Assesses the overall comfort level of a line, including noise levels, air quality, temperature, depth of the line (underground), internet connection, and cleanliness.<br><br>
#     <u><strong>Cost of Living</strong></u>: This metric reflects the affordability of the boroughs served by each line, based on average rent, housing prices, and the cost of living, including pint prices.<br><br>
#     <u><strong>Culture</strong></u>: Measures the cultural richness of the boroughs served by each line, based on the number of cultural sites, box office revenues, and the number of movies filmed in those areas.<br><br><br><br>
#     <u><strong>***DISCLAIMER</strong></u>: This ranking is for educational purposes only. This app was developed for the TUBE project of Data Analytics batch#1922. Team members: Josua Kaufmann, Laura Disney, Xin Ynag and Roudabeh Hatami.*** <br><br><br><br>
#     </p>
# """, unsafe_allow_html=True)
st.markdown("""
    <p style="font-size: 18px; font-weight: bold;">
    Explanation of the metrics:
    </p>
    <p style="font-size: 14px;">
    <u><strong>Security</strong></u>: This metric evaluates the safety of each line, considering the frequency of accidents and crimes across different boroughs.<br><br>
    <u><strong>Crowding</strong></u>: This metric gauges how busy each line is, assessing passenger density during peak hours. <br><br>
    <u><strong>Reliability</strong></u>: Measures the dependability of each line, based on factors like delays, lost customer hours, journey access time, percentage of services operated, and the proportion of kilometers covered.<br><br>
    <u><strong>Connectivity</strong></u>: Evaluates how well each line connects with other transport options, including transfers to underground lines, other public transport, the Night Tube, access lengths, average speeds, and the number of boroughs served.<br><br>
    <u><strong>Comfort</strong></u>: Assesses the overall comfort level of a line, including noise levels, air quality, temperature, depth of the line (underground), internet connection, and cleanliness.<br><br>
    <u><strong>Cost of Living</strong></u>: This metric reflects the affordability of the boroughs served by each line, based on average rent, housing prices, and the cost of living, including pint prices.<br><br>
    <u><strong>Culture</strong></u>: Measures the cultural richness of the boroughs served by each line, based on the number of cultural sites, box office revenues, and the number of movies filmed in those areas.<br><br><br><br>
    <span style="font-size: 12px; font-weight: bold;"><br><br><br><br><br><br><br><br>
    ***DISCLAIMER: This ranking is for educational purposes only. This app was developed for the TUBE project of Data Analytics batch #1922. Team members: Josua Kaufmann, Laura Disney, Xin Yang and Roudabeh Hatami.***
    </span>
    <br><br><br><br>
""", unsafe_allow_html=True)





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

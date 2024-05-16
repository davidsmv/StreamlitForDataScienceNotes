
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests
import json
from st_aggrid import AgGrid

st.set_page_config(layout='centered')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# lottie_airplane = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_jhu1lqdz.json')

with open('streamlit_apps/job_application_example/plane.json', 'r') as file:
    lottie_airplane = json.load(file)
st_lottie(lottie_airplane, speed=0.4, height=100, key="initial")
st.title('Major US Airline Job Application')
st.write('by Tyler Richards')
st.subheader('Question 1: Airport Distance')

st.write("""
    The first exercise asks us 'Given the table of airports and
    locations (in latitude and longitude) below,

    write a function that takes an airport code as input and
    returns the airports listed from nearest to furthest from
    the input airport. There are three steps here:
    1. Load the data
    2. Implement a distance algorithm
    3. Apply the distance formula across all airports other than the input
    4. Return a sorted list of the airports' distances
    """)


# airport_distance_df = pd.read_csv('streamlit_apps/job_application_example/airport_location.csv')
with st.echo():
    #load necessary data
    airport_distance_df = pd.read_csv('streamlit_apps/job_application_example/airport_location.csv')



# Display the Ag-Grid table with specified height and width
AgGrid(
    airport_distance_df, height=250, fit_columns_on_grid_load=True, sortable=True, filter=True
)


st.write("""
From some quick googling, I found that the Haversine distance is
a good approximation for distance. At least good enough to get the
distance between airports! Haversine distances can be off by up to .5%

because the Earth is not actually a sphere. It looks like the latitudes
and longitudes are in degrees, so I'll make sure to have a way to account
for that as well. The Haversine distance formula is labeled below,
followed by an implementation in Python
""")

with st.columns(3)[1]:
    st.image('streamlit_apps/job_application_example/haversine.png')

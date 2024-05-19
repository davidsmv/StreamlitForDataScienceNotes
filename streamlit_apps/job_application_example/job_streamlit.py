
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



with st.echo():
    from math import atan2, cos, radians, sin, sqrt
    def haversine_distance(long1, lat1, long2, lat2,    degrees=False):
        # degrees vs radians
        if degrees == True:
            long1 = radians(long1)
            lat1 = radians(lat1)
            long2 = radians(long2)
            lat2 = radians(lat2)
        # implementing haversine
        a = (
            sin((lat2 - lat1) / 2) ** 2
            + cos(lat1) * cos(lat2) * sin((long2 - long1) / 2) ** 2
        )
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = 6371 * c  # radius of earth in kilometers
        return distance
    


st.write("""
    Now, we need to test out our function! The
    distance between the default points is
    18,986 kilometers, but feel free to try out
    your own points of interest.
    """)
long1 = st.number_input('Longitude 1', value = 2.55)
long2 = st.number_input('Longitude 2', value = 172.00)
lat1 = st.number_input('Latitude 1', value = 49.01)


lat2 = st.number_input('Latitude 2', value = -43.48)
test_distance = haversine_distance(long1 = long1, long2 = long2,
          lat1 = lat1, lat2 = lat2, degrees=True)
st.write('Your distance is: {} kilometers'.format(int(test_distance)))




st.write("""
We have the Haversine distance implemented, and we also have
proven to ourselves that it works reasonably well.
Our next step is to implement this in a function!
""")
with st.echo():
    def get_distance_list(airport_dataframe,
                        airport_code):
        df = airport_dataframe.copy()
        row = df[df.loc[:, "Airport Code"] == airport_code]
        lat = row["Lat"]
        long = row["Long"]
        df = df[df["Airport Code"] != airport_code]
        df["Distance"] = df.apply(
            lambda x: haversine_distance(
                lat1=lat, long1=long, lat2=x.Lat, long2=x.Long, degrees=True
            ),
            axis=1,
        )
        df_to_return = df.sort_values(by="Distance").reset_index()
        return df_to_return["Airport Code"]
    


st.write("""
To use this function, select an airport from the airports provided in the dataframe
and this application will find the distance between each one, and
return a list of the airports ordered from closest to furthest.
""")
selected_airport = st.selectbox('Airport Code', airport_distance_df['Airport Code'])
distance_airports = get_distance_list(
     airport_dataframe=airport_distance_df, airport_code=selected_airport)
st.write('Your closest airports in order are {}'.format(list(distance_airports)))



st.write("""
This all seems to work just fine! There are a few ways I would improve this if I was working on
this for a longer period of time.  
1. I would implement the [Vincenty Distance](https://en.wikipedia.org/wiki/Vincenty%27s_formulae)
instead of the Haversine distance, which is much more accurate but cumbersome to implement.  
2. I would vectorize this function and make it more efficient overall.
Because this dataset is only 7 rows long, it wasn't particularly important,
but if this was a crucial function that was run in production, we would want to vectorize it for speed.
""")
 
import pandas as pd
import streamlit as st
st.title("SF Trees Map")
trees_df = pd.read_csv('streamlit_apps/pretty_trees/trees.csv')
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)
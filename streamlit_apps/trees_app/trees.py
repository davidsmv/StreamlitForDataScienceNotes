import streamlit as st
import pandas as pd
import plotly.express as px


st.title("SF Trees")
st.write(
    """
        This app analyzes trees in San Francisco using
        a dataset kindly provided by SF DPW
    """
)
trees_df = pd.read_csv("trees.csv")
st.write(trees_df)

df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).agg({
    "tree_id": "count"
}))
df_dbh_grouped.columns = ["tree_count"]
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)


trees_df = pd.read_csv("trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)



st.subheader("Plotly Chart")
trees_df = pd.read_csv("trees.csv")
fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)
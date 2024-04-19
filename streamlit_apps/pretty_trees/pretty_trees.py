import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title("SF Trees")

st.write(
    """
    This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW.
    """
)


trees_df = pd.read_csv('streamlit_apps/pretty_trees/trees.csv')

owners = st.sidebar.multiselect(
    "Tree Owner Filter",
    trees_df["caretaker"].unique()
)

graph_color = st.sidebar.color_picker("Graph Colors")
if owners:

    trees_df = trees_df[
        trees_df["caretaker"].isin(owners)]
    

edited_df = st.data_editor(trees_df) 
trees_df.loc[edited_df.index] = edited_df
if st.button("Save data and overwrite:"):
    trees_df.to_csv("trees.csv", index=False)
    st.write("Saved!")

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

# col1, col2, col3 = st.columns(3, gap="large")

# with col1:
#     st.line_chart(df_dbh_grouped)
# with col2:
#     st.bar_chart(df_dbh_grouped)
# with col3:
#     st.area_chart(df_dbh_grouped)




tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])

with tab1:
    st.line_chart(df_dbh_grouped, 
        color=[graph_color])
with tab2:
    st.bar_chart(df_dbh_grouped,
                 color=[graph_color])
with tab3:
    st.area_chart(df_dbh_grouped,
                  color=[graph_color])



 
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])

 
st.map(trees_df)
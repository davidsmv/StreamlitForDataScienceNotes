import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# # st.write("Hello World")
# binom_dist = np.random.binomial(1, .5, 1000)
# # st.write(np.mean(binom_dist))

# list_of_means = []

# for i in range(0, 1000):
#     list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

# fig, ax = plt.subplots()
# ax = plt.hist(list_of_means)
# st.pyplot(fig)


st.title("Ilustrating the Central Limit Theorem with Streamlit")
st.subheader("An app by David Martínez")
st.write(('This app simulates a thousand coin flips using the chance of heads input below, '
     'and then samples with replacement from that population and plots the histogram of the'
     ' means of the samples in order to illustrate the central limit theorem!'))
perc_heads = st.number_input(
    label="Chance of coins landing on Heads",
    min_value=0.0,
    max_value=1.0,
    value=0.5)

graph_title = st.text_input(label="Graph Title")


binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []

for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

fig, ax = plt.subplots()
plt.hist(list_of_means, range=[0,1])
plt.title(graph_title)
st.pyplot(fig)
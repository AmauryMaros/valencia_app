import streamlit as st
from scripts import nugent, pH_plot

st.sidebar.subheader("Contact")
st.sidebar.write("mfrance@som.umaryland.edu")

st.subheader("Nugent analysis", divider='grey')
st.pyplot(nugent.stacked_fig)

st.subheader("pH analysis", divider='grey')
st.pyplot(pH_plot.stacked_fig)
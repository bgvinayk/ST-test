import streamlit as st
import pandas as pd

st.title("Cooling Water Program Recommendation")
st.markdown("## Enter cooling tower parameters")
st.subheader("MECHANICAL CONDITIONS")


costProducts = pd.read_csv('https://raw.githubusercontent.com/bgvinayk/ST-test/main/try.py',index=0)

st.subheader(costProducts[0][0])

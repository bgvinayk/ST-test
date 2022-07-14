import streamlit as st
import pandas as pd

st.title("Cooling Water Program Recommendation")
st.markdown("## Enter cooling tower parameters")
st.subheader("MECHANICAL CONDITIONS")


costProducts = pd.read_csv('https://github.com/bgvinayk/ST-test/blob/main/Model_Product_Costs.csv')

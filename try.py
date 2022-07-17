import streamlit as st
import pandas as pd
from scipy.optimize import fsolve
from reaktoro import *

# db = PhreeqcDatabase("minteq.v4.dat")

st.title("Cooling Water Program Recommendation")
st.markdown("## Enter cooling tower parameters")
st.subheader("MECHANICAL CONDITIONS")
  
costProducts = pd.read_csv('https://raw.githubusercontent.com/bgvinayk/ST-test/main/Model_Product_Costs.csv')

st.subheader(str(costProducts['PRODUCT'][1]))

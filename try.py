import streamlit as st
import pandas as pd
from scipy.optimize import fsolve
import reaktoro as rkt

st.title("Cooling Water Program Recommendation")
st.markdown("## Enter cooling tower parameters")
st.subheader("MECHANICAL CONDITIONS")

db1 = rkt.ThermoFunDatabase("slop98")
db = rkt.PhreeqcDatabase("minteq.v4.dat")
  
costProducts = pd.read_csv('https://raw.githubusercontent.com/bgvinayk/ST-test/main/Model_Product_Costs.csv')

st.subheader(str(costProducts['PRODUCT'][1]))

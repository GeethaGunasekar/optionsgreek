# Importing the necessary Python modules.
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from scipy.stats import norm

from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import delta

st.header("Option Price Calculator")
r=0.10
st1=st.sidebar.number_input("Enter the Strike price:")
k=st.sidebar.number_input("Enter the Option Premium(spot price)")
T=240/365

sigma=st.sidebar.number_input("Enter the volatility of the asset")

put=st.sidebar.radio("select C for Call and P for put",("c","p"))


S=float(st1)
K=float(k)
sigma=float(sigma)

def blackScholes(r, S, K, T, sigma, type="c"):
    st.subheader("Calculate BS price of call/put")
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if type == "c":
        st.write("Calculate BS price of call")
        price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
    elif type == "p":
       st.write("Calculate BS price of put")
       price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
    st.write("Option Price",round(price,3),"\n Option Price(module cal)",round(bs(type, S, K, T, r, sigma),3))
   
def delta_calc2(r, S, K, T, sigma, type="c"):
    st.subheader("Calculate delta of an option")
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    if type == "c":

        delta_calc = norm.cdf(d1, 0, 1)
    elif type == "p":
        delta_calc = -norm.cdf(-d1, 0, 1)
    st.write("Time decay value",delta_calc)
    st.write("Time decay value(module cal)",delta(type, S, K, T, r, sigma))



if st.sidebar.button("calculate"):
	blackScholes(r, S, K, T, sigma, type="p")
	delta_calc2(r, S, K, T, sigma, type="c")
	
   
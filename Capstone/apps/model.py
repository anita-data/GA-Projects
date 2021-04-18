import streamlit as st
import pickle
import pandas as pd
import numpy as np 
from PIL import Image

pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

# Text/Title
def app():
    st.title("Model Comparison")
    st.write("Welcome to the technical part of churn prediction")

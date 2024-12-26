import os 
from dotenv import load_dotenv
load_dotenv()
#basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))
#PASSWORD_APP = os.getenv("PASSWORD_APP")
import streamlit as st
st.text_input("Please enter the password to use this App", key="in_password", type="password")
app_password = st.session_state.in_password
if app_password:
    if (app_password != "abc"):
        st.write("Password incorrect, please try again")
    else:
        st.write("password correct")
